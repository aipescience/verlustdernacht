app = angular.module('data',[]);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.factory('DataService', ['$http','$window',function($http,$window) {

    var baseurl = angular.element('meta[name="baseurl"]').attr('content');

    var service = {};

    var urls = {
        'locations': baseurl + 'api/locations/',
        'nights': baseurl + 'api/nights/',
        'measurements': baseurl + 'api/measurements/',
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

    service.init = function() {
        // fetch locations
        $http.get(urls.locations).success(function(response) {
            service.locations = response;
            service.location = service.locations[0];

            service.axes = {
                xmin: new Date('2000-01-01'),
                xmax: new Date('2000-01-01'),
                ymin: 22,
                ymax: 5
            };
            service.axes.xmin.setHours(20);
            service.axes.xmax.setDate(service.axes.xmax.getDate() + 1);
            service.axes.xmax.setHours(7);

            // fetch last night
            $http.get(urls.nights + 'latest/').success(function(response) {
                service.night = response;

                service.setDate(response.date);
                service.fetchMeasurements();
            });
        });
    };

    service.fetchNight = function() {
        var config = {
            params: {
                date: service.date
            }
        };

        $http.get(urls.nights, config).success(function(response) {
            if (response.length) {
                service.night = response[0];

                service.setDate(service.night.date);
                service.fetchMeasurements();
            } else {
                service.count = 0;
                service.measurements = [];

                service.drawPlot();
            }
        });
    };

    service.fetchMeasurements = function() {
        var after = new Date(service.night.date);
        after.setHours(12);
        var before = new Date(after);
        before.setDate(before.getDate() + 1);

        var config = {
            params: {
                location: service.location.slug,
                after: after,
                before: before,
                every: 10
            }
        };

        $http.get(urls.measurements, config).success(function(response) {
            service.count = response.count;
            service.measurements = response.measurements;

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

        var data = service.measurements,
            key = 'magnitude';

        if (data.length === 0) return;

        var margin = {top: 10, right: 20, bottom: 40, left: 60},
            width = 688.5 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        var xScale = d3.time.scale.utc()
                        .domain([service.axes.xmin, service.axes.xmax])
                        .range([0, width]),
            yScale = d3.scale.linear()
                        .domain([service.axes.ymin, service.axes.ymax])
                        .range([height, 0]);

        var xTicks = d3.time.hours,
            xTickFormat = d3.time.format('%H:00');

        var xAxis = d3.svg.axis().scale(xScale)
                        .orient('bottom')
                        .ticks(xTicks)
                        .tickFormat(xTickFormat),
            yAxis = d3.svg.axis().scale(yScale)
                        .orient('left');

        d3.selectAll("svg > *").remove();

        var svg = d3.select('#plot')
                        .append("g")
                        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        var x = {};
        angular.forEach(['sunset', 'sunrise', 'civil_dusk', 'civil_dawn', 'nautical_dusk', 'nautical_dawn', 'astronomical_dusk', 'astronomical_dawn', 'nadir'], function (key) {
            if (service.night[key] !== null) {
                x[key] = xScale(new Date(service.night[key]));
            }
        });

        if (angular.isDefined(x.sunset) && angular.isDefined(x.sunrise)) {
        svg.append('g').append('rect')
            .attr("x", x.sunset)
            .attr("y", 0)
            .attr("width", x.sunrise - x.sunset)
            .attr("height", height)
            .attr('class', 'civil-twilight');
        }
        if (angular.isDefined(x.civil_dusk) && angular.isDefined(x.civil_dawn)) {
        svg.append('g').append('rect')
            .attr("x", x.civil_dusk)
            .attr("y", 0)
            .attr("width", x.civil_dawn - x.civil_dusk)
            .attr("height", height)
            .attr('class', 'nautical-twilight');
        }
        if (angular.isDefined(x.nautical_dusk) && angular.isDefined(x.nautical_dawn)) {
            svg.append('g').append('rect')
                .attr("x", x.nautical_dusk)
                .attr("y", 0)
                .attr("width", x.nautical_dawn - x.nautical_dusk)
                .attr("height", height)
                .attr('class', 'astronomical-twilight');
        }
        if (angular.isDefined(x.astronomical_dusk) && angular.isDefined(x.astronomical_dawn)) {
        svg.append('g').append('rect')
            .attr("x", x.astronomical_dusk)
            .attr("y", 0)
            .attr("width", x.astronomical_dawn - x.astronomical_dusk)
            .attr("height", height)
            .attr('class', 'night');
        }
        svg.append('g').call(xAxis)
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + height + ')');
        svg.append('g').call(yAxis)
            .attr('class', 'axis')
            .attr('transform', 'translate(0, 0)');
        svg.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(-40,"+(height/2)+")rotate(-90)")
            .attr('class', 'axis')
            .text("Helligkeit in Mag");
        svg.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate("+ (width/2) +"," + (height+40) + ")")
            .attr('class', 'axis')
            .text("Uhrzeit");

        var line = d3.svg.line()
            .x(function (d) { return xScale(new Date(d.timestamp)); })
            .y(function (d) { return yScale(d[key]); })
            .interpolate('basis');

        svg.append('g').append("path")
            .attr("d", line(data))
            .attr('class', 'data');
    };

    return service;
}]);

app.controller('DataController', ['$scope','DataService',function($scope, DataService) {

    $scope.service = DataService;
    $scope.service.init();

}]);
