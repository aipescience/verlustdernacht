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

            // fetch last night
            $http.get(urls.nights + 'latest/').success(function(response) {
                service.night = response;
                service.date = new Date(response.date);

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

    service.drawPlot = function() {

        d3.selectAll("svg > *").remove();

        var data = service.measurements,
            key = 'magnitude';

        if (data.length === 0) return;

        var margin = {top: 10, right: 10, bottom: 20, left: 20},
            width = 320 - margin.left - margin.right,
            height = 240 - margin.top - margin.bottom;

        var xMin = new Date(getMin(data, 'timestamp')),
            xMax = new Date(getMax(data, 'timestamp')),
            yMin = Math.ceil(getMax(data, key)),
            yMax = getMin(data, key);

        var xScale = d3.time.scale.utc().domain([xMin, xMax]).range([0, width]),
            yScale = d3.scale.linear().domain([yMin, yMax]).range([height, 0]);

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

        svg.append('g').call(xAxis)
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + height + ')');
        svg.append('g').call(yAxis)
            .attr('class', 'axis')
            .attr('transform', 'translate(0, 0)');

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
