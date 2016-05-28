app = angular.module('data',[]);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.factory('DataService', ['$http','$window',function($http,$window) {

    var baseurl = angular.element('meta[name="baseurl"]').attr('content');
    var staticurl = angular.element('meta[name="staticurl"]').attr('content');

    var service = {};

    var urls = {
        'locations': baseurl + 'api/locations/',
        'nights': baseurl + 'api/nights/',
        'measurements': baseurl + 'api/measurements/',
        'moonpositions': baseurl + 'api/moonpositions/'
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

    service.init = function() {
        // fetch locations
        $http.get(urls.locations).success(function(response) {
            service.locations = response;
            service.location = service.locations[0];

            service.axes = {
                xmin: new Date('2000-01-01'),
                xmax: new Date('2000-01-01'),
                ymin: 22,
                ymax: 5,
                y2min: 0,
                y2max: 29
            };
            service.axes.xmin.setHours(20);
            service.axes.xmax.setDate(service.axes.xmax.getDate() + 1);
            service.axes.xmax.setHours(7);

            // fetch last night
            $http.get(urls.nights + 'latest/').success(function(response) {
                service.night = response;
                service.moon_url = getMoonUrl(service.night.moon_phase);

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
                service.moon_url = getMoonUrl(service.night.moon_phase);

                service.setDate(service.night.date);
                service.fetchMeasurements();
            } else {
                service.night = false;
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

            config.params.every = 1;
            $http.get(urls.moonpositions, config).success(function(response) {
                service.moonpositions = response.moonpositions;
                service.drawPlot();
            });
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

        var xTicks = d3.time.hours,
            xTickFormat = d3.time.format('%H:00');

        var xAxis = d3.svg.axis().scale(xScale)
                        .ticks(xTicks)
                        .tickFormat(xTickFormat),
            x2Axis = d3.svg.axis().scale(x2Scale),
            yAxis = d3.svg.axis().scale(yScale),
            y2Axis = d3.svg.axis().scale(y2Scale);

        var x = {};
        angular.forEach(['sunset', 'sunrise', 'civil_dusk', 'civil_dawn', 'nautical_dusk', 'nautical_dawn', 'astronomical_dusk', 'astronomical_dawn', 'nadir'], function (key) {
            if (service.night[key] !== null) {
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
