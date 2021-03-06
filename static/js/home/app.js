app = angular.module('home',['ngResource'])

.config(['$httpProvider', '$interpolateProvider', '$resourceProvider', function($httpProvider, $interpolateProvider, $resourceProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $resourceProvider.defaults.actions.paginate = {
        method: 'GET',
        isArray: false
    };
}])

.factory('HomeService', ['$resource', '$window', function($resource, $window) {

    var baseurl = angular.element('meta[name="baseurl"]').attr('content');
    var staticurl = angular.element('meta[name="staticurl"]').attr('content');

    var resources = {
        locations: $resource(baseurl + 'api/locations/:id/'),
        nights: $resource(baseurl + 'api/nights/:list_route/:id/'),
        measurements: $resource(baseurl + 'api/measurements/:id/')
    };

    var service = {};

    service.init = function() {
        service.loading = true;
        service.no_data = false;

        resources.locations.query(function(response) {
            if (response.length > 0) {
                service.location = response[0];

                resources.nights.query({
                    list_route: 'latest',
                    location: service.location.slug
                }, function(response) {
                    service.night = response[0];
                    service.date = new Date(service.night.date);

                    var now = new Date();
                    if (service.date.getDate() === now.getDate() &&
                        service.date.getMonth() === now.getMonth() &&
                        service.date.getYear() === now.getYear()) {
                        service.today = true;
                    } else {
                        service.today = false;
                    }

                    var after = new Date(service.date.getFullYear(),
                                         service.date.getMonth(),
                                         service.date.getDate(), 12),
                        before = new Date(service.date.getFullYear(),
                                          service.date.getMonth(),
                                          service.date.getDate() + 1, 12);

                    resources.measurements.paginate({
                        location: service.location.slug,
                        after: after,
                        before: before,
                        every: 100
                    }, function(response) {
                        service.measurements = response.measurements;

                        service.loading = false;
                        service.no_data = false;

                        service.draw();
                    });

                }, function() {
                    service.loading = false;
                    service.no_data = true;
                });

            } else {
                service.loading = false;
                service.no_data = true;
            }
        });
    };

    service.draw = function() {
        var margin = {top: 10, right: 10, bottom: 20, left: 30},
            width = 289 - margin.left - margin.right,
            height = 216 - margin.top - margin.bottom,
            separator = height * 0.2;

        var xmin = new Date(service.date.getFullYear(),
                            service.date.getMonth(),
                            service.date.getDate(), 15),
            xmax = new Date(service.date.getFullYear(),
                            service.date.getMonth(),
                            service.date.getDate() + 1, 9),
            ymin = 22,
            ymax = 5;

        var xScale = d3.scaleUtc()
                        .domain([xmin, xmax])
                        .range([0, width]),
            yScale = d3.scaleLinear()
                        .domain([ymin, ymax])
                        .range([height, 0]);

        var xAxis_bottom = d3.axisBottom(xScale).ticks(4).tickFormat(d3.timeFormat('%H:00')),
            xAxis_top = d3.axisTop(xScale).ticks(4).tickFormat(''),
            yAxis_left = d3.axisLeft(yScale).ticks(4),
            yAxis_right = d3.axisRight(yScale).ticks(4).tickFormat('');

        var plot = d3.select('#plot')
            .append("g")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        var clip = plot.append('defs').append('clipPath')
            .attr('id', 'clip')
            .append('rect')
            .attr('x', '0')
            .attr('y', '0')
            .attr('width', width)
            .attr('height', height);

        var area = plot.append('g')
            .attr('clip-path', 'url(' + $window.location.href + '#clip)');

        plot.append('g').call(yAxis_left)
            .attr('class', 'axis')
            .attr('fill', '#fff')
            .attr('transform', 'translate(0, 0)');
        plot.append('g').call(yAxis_right)
            .attr('class', 'axis')
            .attr('transform', 'translate(' + width + ', 0)');

        plot.append('g').call(xAxis_bottom)
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + height + ')');
        plot.append('g').call(xAxis_top)
            .attr('class', 'axis')
            .attr('transform', 'translate(0,0)');

        var line = d3.line()
            .x(function (d) { return xScale(new Date(d.timestamp)); })
            .y(function (d) { return yScale(d['magnitude']); });

        area.append('g').append("path")
            .attr("d", line(service.measurements))
            .attr('class', 'data');
    };

    service.data = function () {
        $window.location = 'daten';
    };

    return service;
}])

.controller('HomeController', ['$scope', 'HomeService', function($scope, HomeService) {

    $scope.service = HomeService;
    $scope.service.init();

}]);
