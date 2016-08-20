app.factory('DataService', ['$resource', '$q', '$location', 'PlotService', function($resource, $q, $location, PlotService) {

    var baseurl = angular.element('meta[name="baseurl"]').attr('content');
    var staticurl = angular.element('meta[name="staticurl"]').attr('content');

    var resources = {
        locations: $resource(baseurl + 'api/locations/:id/'),
        nights: $resource(baseurl + 'api/nights/:list_route/:id/'),
        measurements: $resource(baseurl + 'api/measurements/:id/'),
        moonpositions: $resource(baseurl + 'api/moonpositions/:id/'),

    };

    function getMin(data, key) {
        return data.reduce(function(prev, curr) {
            return prev[key] < curr[key] ? prev : curr;
        })[key];
    }

    function getMax(data, key) {
        return data.reduce(function(prev, curr) {
            return prev[key] > curr[key] ? prev : curr;
        })[key];
    }

    function getMoonUrl(moon_phase) {
        var moon_string = Math.floor(moon_phase * 30).toString();
        return staticurl + 'img/moon/moon' + moon_string + '_sm.png';
    }

    var service = {
        location: null,
        date: null,
        month: null,
        axes: {
            xmin: new Date(2000, 1, 1, 15),
            xmax: new Date(2000, 1, 2, 9),
            ymin: 22,
            ymax: 5,
            y2min: 0,
            y2max: 70
        },
        plot: PlotService
    };

    service.init = function() {

        resources.locations.query(function(response) {
            service.locations = response;
            service.parseLocation();
            service.initView();
        });
    };

    service.initView = function() {
        if (service.month) {
            service.fetchMonth();
        } else {
            service.fetchNight();
        }
    };

    service.parseLocation = function() {
        var match,
            location_slug = null,
            path = $location.path();

        m1 = path.match(/^\/([A-Za-z0-9\_\-]+)\/(\d{4}-\d{2}-\d{2})/);
        m2 = path.match(/^\/([A-Za-z0-9\_\-]+)\/(\d{4}-\d{2})/);
        m3 = path.match(/^\/([A-Za-z0-9\_\-]+)/);

        if (m1) {
            location_slug = m1[1];
            service.date = new Date(m1[2]);
        } else if (m2) {
            location_slug = m2[1];
            service.month = new Date(m2[2]);
        } else if (m3) {
            location_slug = m3[1];
        }

        angular.forEach(service.locations, function(location) {
            if (location.slug == location_slug) {
                service.location = location;
            }
        });

        if (service.location === null) {
            service.location = service.locations[0];
        }
    };

    service.updateLocation = function() {
        if (service.month) {
            $location.path('/' + service.location.slug + '/' + moment(service.month).format('YYYY-MM'));
        } else if (service.date) {
            $location.path('/' + service.location.slug + '/' + moment(service.date).format('YYYY-MM-DD'));
        }
    };

    service.updateAxes = function() {
        service.axes.xmin = new Date(
            service.date.getFullYear(),
            service.date.getMonth(),
            service.date.getDate(),
            service.axes.xmin.getHours(),
            service.axes.xmin.getMinutes()
        );
        service.axes.xmax = new Date(
            service.date.getFullYear(),
            service.date.getMonth(),
            service.date.getDate() + 1,
            service.axes.xmax.getHours(),
            service.axes.xmax.getMinutes()
        );
    };

    service.fetchNight = function() {
        if (angular.isDefined(service.date) && service.date) {
            resources.nights.paginate({
                location: service.location.slug,
                after: moment(service.date).format('YYYY-MM-DD'),
                before: moment(service.date).format('YYYY-MM-DD')
            }, function(response) {
                if (response.nights.length) {
                    service.night = response.nights[0];
                    service.moon_url = getMoonUrl(service.night.moon_phase);
                    service.updateLocation();
                    service.updateAxes();
                    service.fetchMeasurements();
                } else {
                    service.night = false;
                    service.moon_url = false;
                    service.updateLocation();
                    service.measurements = [];
                }
            });
        } else {
            // fetch last night
            resources.nights.query({
                list_route: 'latest',
                location: service.location.slug
            }, function(response) {
                service.night = response[0];
                service.date = new Date(service.night.date);

                service.moon_url = getMoonUrl(service.night.moon_phase);
                service.updateLocation();
                service.updateAxes();
                service.fetchMeasurements();
            }, function() {
                service.night = false;
                service.date = false;
            });
        }
    };

    service.fetchMonth = function() {
        service.updateLocation();

        service.nights = [];

        var dates = [];
        var date = new Date(service.month);
        while (date.getMonth() === service.month.getMonth()) {
            dates.push(date);
            date = new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1);
        }

        var promises = [];
        service.nights = [];
        angular.forEach(dates, function(date) {
            var night = {
                date: date
            };

            promises.push(resources.measurements.paginate({
                location: service.location.slug,
                after: new Date(date.getFullYear(), date.getMonth(), date.getDate(), 12),
                before: new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1, 12),
                every: 60
            }, function(response) {
                night.measurements = response.measurements;
            }).$promise);

            service.nights.push(night);
        });

        $q.all(promises).then(function() {
            service.plot.drawMonth(service, function(night) {
                service.showNight(night);
            });
        });
    };

    service.fetchMeasurements = function() {
        var after = new Date(service.date.getFullYear(), service.date.getMonth(), service.date.getDate(), 12),
            before = new Date(service.date.getFullYear(), service.date.getMonth(), service.date.getDate() + 1, 12);

        var config = {
            location: service.location.slug,
            after: after,
            before: before,
            every: 10
        };

        var measurements_promise = resources.measurements.paginate(config, function(response) {
            service.measurements = response.measurements;
        }).$promise;

        config.every = 1;
        var moonpositions_promise = resources.moonpositions.paginate(config, function(response) {
            service.moonpositions = response.moonpositions;
        }).$promise;

        $q.all([measurements_promise, moonpositions_promise]).then(function() {
            service.plot.drawNight(service);
        });
    };

    service.prev = function() {
        var date = angular.copy(service.date);
        date.setDate(date.getDate() - 1);

        service.date = date;
        service.fetchNight();
    };

    service.next = function() {
        var date = angular.copy(service.date);
        date.setDate(date.getDate() + 1);

        service.date = date;
        service.fetchNight();
    };

    service.showNight = function(night) {
        service.date = new Date(night.date);
        service.month = false;
        service.fetchNight();
    };

    service.showMonth = function() {
        service.month = new Date(service.date.getFullYear(), service.date.getMonth());
        service.date = false;
        service.fetchMonth();
    };

    return service;
}]);
