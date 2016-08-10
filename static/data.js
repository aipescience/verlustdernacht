app = angular.module('data',['ngResource']);

app.config(['$httpProvider', '$interpolateProvider', '$locationProvider', '$resourceProvider', function($httpProvider, $interpolateProvider, $locationProvider, $resourceProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $locationProvider.html5Mode(true);
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $resourceProvider.defaults.actions.paginate = {
        method: 'GET',
        isArray: false
    };
}]);

app.factory('DataService', ['$resource', '$q', '$window', '$location', function($resource, $q, $window, $location) {

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

    var service = {};

    service.init = function() {
        // fetch locations
        resources.locations.query(function(response) {
            service.locations = response;
            service.location = service.locations[0];

            service.axes = {
                xmin: new Date('2000-01-01'),
                xmax: new Date('2000-01-01'),
                ymin: 22,
                ymax: 5,
                y2min: 0,
                y2max: 70
            };
            service.axes.xmin.setHours(15);
            service.axes.xmax.setDate(service.axes.xmax.getDate() + 1);
            service.axes.xmax.setHours(9);

            // get the current date form the url
            var date_string = $location.path().replace(/\//g,'');
            var date = new Date(date_string);

            if (isNaN(date) === false) {
                service.date = date;
            } else {
                service.date = null;
            }

            service.fetchNight();
        });
    };

    service.fetchNight = function() {
        if (angular.isDefined(service.date) && service.date) {
            resources.nights.query({date: service.date}, function(response) {
                if (response.length) {
                    service.night = response[0];

                    service.moon_url = getMoonUrl(service.night.moon_phase);
                    service.setDate(service.night.date);
                    service.fetchMeasurements();
                } else {
                    service.night = false;
                    $location.path('/');

                    service.measurements = [];
                    service.drawPlot();
                }
            });
        } else {
            // fetch last night
            resources.nights.query({list_route: 'latest'}, function(response) {
                service.night = response[0];

                service.moon_url = getMoonUrl(service.night.moon_phase);
                service.setDate(service.night.date);
                service.fetchMeasurements();
            });
        }
    };

    service.fetchMeasurements = function() {
        var after = new Date(service.night.date);
        after.setHours(12);
        var before = new Date(after);
        before.setDate(before.getDate() + 1);

        var config = {
            location: service.location.slug,
            after: after,
            before: before,
            every: 10
        };

        var p1 = resources.measurements.paginate(config, function(response) {
            service.measurements = response.measurements;
        }).$promise;

        config.every = 1;
        var p2 = resources.moonpositions.paginate(config, function(response) {
            service.moonpositions = response.moonpositions;
        }).$promise;

        $q.all([p1, p2]).then(function() {
            service.drawPlot();
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

    service.setDate = function(date) {
        service.date = new Date(date);

        $location.path('/' + date);

        var xmin = new Date(date);
        xmin.setHours(service.axes.xmin.getHours());
        xmin.setMinutes(service.axes.xmin.getMinutes());
        service.axes.xmin = xmin;

        var xmax = new Date(date);
        xmax.setDate(xmax.getDate() + 1);
        xmax.setHours(service.axes.xmax.getHours());
        xmax.setMinutes(service.axes.xmax.getMinutes());
        service.axes.xmax = xmax;
    };

    service.drawPlot = function() {

        d3.selectAll("svg > *").remove();

        if (service.measurements.length === 0) return;

        var margin = {top: 50, right: 30, bottom: 50, left: 60},
            width = 688.5 - margin.left - margin.right,
            height = 688.5 - margin.top - margin.bottom,
            separator = height * 0.2;

        var time = service.date.getTime();

        var x2min = (service.axes.xmin.getTime() - time) / 86400000.0,
            x2max = (service.axes.xmax.getTime() - time) / 86400000.0;

        var xScale = d3.time.scale.utc()
                        .domain([service.axes.xmin, service.axes.xmax])
                        .range([0, width]),
            x2Scale = d3.scale.linear()
                        .domain([x2min, x2max])
                        .range([0, width]),
            yScale = d3.scale.linear()
                        .domain([service.axes.ymin, service.axes.ymax])
                        .range([height - separator, 0]),
            y2Scale = d3.scale.linear()
                        .domain([service.axes.y2min, service.axes.y2max])
                        .range([height, height - separator]);

        var xAxis = d3.svg.axis().scale(xScale).ticks(6).tickFormat(d3.time.format('%H:00')),
            x2Axis = d3.svg.axis().scale(x2Scale),
            yAxis = d3.svg.axis().scale(yScale),
            y2Axis = d3.svg.axis().ticks(4).scale(y2Scale);

        var x = {};
        angular.forEach(['sunset', 'sunrise', 'civil_dusk', 'civil_dawn', 'nautical_dusk', 'nautical_dawn', 'astronomical_dusk', 'astronomical_dawn', 'nadir'], function (key) {
            if (angular.isDefined(service.night[key]) && service.night[key] !== null ) {
                x[key] = xScale(new Date(service.night[key]));
            }
        });

        d3.selectAll("svg > *").remove();

        var svg = d3.select('#plot')
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        svg.append('clipPath').attr('id', 'clip')
            .append('rect')
            .attr('x', '0')
            .attr('y', '0')
            .attr('width', width)
            .attr('height', height);

        if (angular.isDefined(x.sunset) && angular.isDefined(x.sunrise)) {
        svg.append('g').append('rect')
            .attr("x", x.sunset)
            .attr("y", 0)
            .attr("width", x.sunrise - x.sunset)
            .attr("height", height)
            .attr('clip-path', "url(#clip)")
            .attr('class', 'civil-twilight');
        }
        if (angular.isDefined(x.civil_dusk) && angular.isDefined(x.civil_dawn)) {
        svg.append('g').append('rect')
            .attr("x", x.civil_dusk)
            .attr("y", 0)
            .attr("width", x.civil_dawn - x.civil_dusk)
            .attr("height", height)
            .attr('clip-path', "url(#clip)")
            .attr('class', 'nautical-twilight');
        }
        if (angular.isDefined(x.nautical_dusk) && angular.isDefined(x.nautical_dawn)) {
            svg.append('g').append('rect')
                .attr("x", x.nautical_dusk)
                .attr("y", 0)
                .attr("width", x.nautical_dawn - x.nautical_dusk)
                .attr("height", height)
                .attr('clip-path', "url(#clip)")
                .attr('class', 'astronomical-twilight');
        }
        if (angular.isDefined(x.astronomical_dusk) && angular.isDefined(x.astronomical_dawn)) {
            svg.append('g').append('rect')
                .attr("x", x.astronomical_dusk)
                .attr("y", 0)
                .attr("width", x.astronomical_dawn - x.astronomical_dusk)
                .attr("height", height)
                .attr('clip-path', "url(#clip)")
                .attr('class', 'night');
        }

        svg.append('g').call(xAxis.orient('bottom'))
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + height + ')');
        svg.append('g').call(xAxis.orient('bottom').tickFormat(''))
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + (height - separator) + ')');
        svg.append('g').call(x2Axis.orient('top'))
            .attr('class', 'axis')
            .attr('transform', 'translate(0,0)');

        svg.append('g').call(yAxis.orient('left'))
            .attr('class', 'axis')
            .attr('transform', 'translate(0, 0)');
        svg.append('g').call(yAxis.orient('right').tickFormat(''))
            .attr('class', 'axis')
            .attr('transform', 'translate(' + width + ', 0)');

        svg.append('g').call(y2Axis.orient('left'))
            .attr('class', 'axis')
            .attr('transform', 'translate(0, 0)');
        svg.append('g').call(y2Axis.orient('right').tickFormat(''))
            .attr('class', 'axis')
            .attr('transform', 'translate(' + width + ', 0)');

        // x labels
        svg.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(" + (width/2) +"," + (height+40) + ")")
            .attr('class', 'axis')
            .text("Zeit t");
        svg.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(" + (width/2) +",-30)")
            .attr('class', 'axis')
            .text('MJD (' + service.night.mjd + ')');

        // y labels
        svg.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(-40," + ((height - separator)/2) + ")rotate(-90)")
            .attr('class', 'axis')
            .text("Helligkeit m [Mag]");
        svg.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(-40," + ((height - separator) + (separator)/2) + ")rotate(-90)")
            .attr('class', 'axis')
            .text('Höhe des Mondes');

        var line = d3.svg.line()
            .x(function (d) { return xScale(new Date(d.timestamp)); })
            .y(function (d) { return yScale(d['magnitude']); })
            .interpolate('basis');

        var line2 = d3.svg.line()
            .x(function (d) { return xScale(new Date(d.timestamp)); })
            .y(function (d) { return y2Scale(d['altitude']); })
            .interpolate('basis');

        svg.append('g').append("path")
            .attr("d", line(service.measurements))
            .attr('clip-path', "url(#clip)")
            .attr('class', 'data');

        svg.append('g').append("path")
            .attr("d", line2(service.moonpositions))
            .attr('clip-path', "url(#clip)")
            .attr('class', 'data');
    };

    return service;
}]);

app.controller('DataController', ['$scope','DataService',function($scope, DataService) {

    $scope.service = DataService;
    $scope.service.init();

}]);
