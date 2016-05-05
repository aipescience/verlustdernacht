app = angular.module('data',[]);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.factory('DataService', ['$http','$window',function($http,$window) {

    var service = {};

    var urls = {
        'locations': '/api/locations/',
        'measurements': '/api/measurements/',
    };

    function getDate() {
        var date = new Date();

        // if (date.getHours() > 12) {
        //     date.setDate(date.getDate() - 1);
        // }
        date.setHours(12, 0, 0);
        return date;
    }

    function fetchLocations() {
        $http.get(urls.locations).success(function(response) {
            service.locations = response;

            if (angular.isUndefined(service.location)) {
                service.location = service.locations[0];
                fetchMeasurements();
            }
        });
    }

    function fetchMeasurements() {
        var before = angular.copy(service.date);
        before.setDate(before.getDate() + 1);

        var config = {
            params: {
                location: service.location.slug,
                after: service.date,
                before: before
            }
        };

        $http.get(urls.measurements, config).success(function(response) {
            service.measurements = response;
            drawPlot();
        });
    }

    function drawPlot() {

        var margin = {top: 10, right: 10, bottom: 30, left: 50},
            width = 640 - margin.left - margin.right,
            height = 480 - margin.top - margin.bottom;

        var xMin = service.date;
        var xMax = angular.copy(service.date);
        xMax.setDate(xMax.getDate() + 1);

        var yMin = 20,
            yMax = 60;

        var xScale = d3.time.scale.utc()
                        .domain([xMin, xMax])
                        .range([0, width]),
            yScale = d3.scale.linear()
                        .domain([yMin, yMax])
                        .range([height, 0]);

        var ticks = d3.time.hours,
            tickFormat = d3.time.format('%H');

        var xAxis = d3.svg.axis().scale(xScale)
                        .orient('bottom')
                        .ticks(ticks)
                        .tickFormat(tickFormat),
            yAxis = d3.svg.axis().scale(yScale)
                        .orient('left');

        var svg = d3.select('#plot')
                        .append("g")
                        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        svg.append('g').call(xAxis)
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + height + ')');
        svg.append('g').call(yAxis)
            .attr('class', 'axis')
            .attr('transform', 'translate(0, 0)');

        // svg.append('g').selectAll('circle')
        //     .data(service.measurements)
        //     .enter()
        //         .append('circle')
        //         .attr('class', 'data')
        //         .attr('cx', function (d) { return xScale(new Date(d.timestamp)); })
        //         .attr('cy', function (d) { return yScale(d.temperature); });

        var line = d3.svg.line()
            .x(function (d) { return xScale(new Date(d.timestamp)); })
            .y(function (d) { return yScale(d.temperature); })
            .interpolate('basis');

        svg.append('g').append("path")
            .attr("d", line(service.measurements))
            .attr('class', 'data');
    };


    service.init = function() {

        service.date = getDate();
        fetchLocations();

    };

    return service;
}]);

app.controller('DataController', ['$scope','DataService',function($scope, DataService) {

    $scope.service = DataService;
    $scope.service.init();

}]);
