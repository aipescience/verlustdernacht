app.factory('PlotService', ['$window', '$filter', function($window, $filter) {

    plot_service = {};

    plot_service.clear = function() {
        d3.selectAll("svg > *").remove();
    };

    plot_service.drawNight = function(service) {

        service.plot.clear();

        if (service.measurements.length === 0) return;

        var margin = {top: 50, right: 30, bottom: 50, left: 60},
            width = 688.5 - margin.left - margin.right,
            height = 688.5 - margin.top - margin.bottom,
            separator = height * 0.2;

        var xmin = service.axes.xmin,
            xmax = service.axes.xmax,
            ymin = service.axes.ymin,
            ymax = service.axes.ymax,
            x2min = (service.axes.xmin.getTime() - service.date.getTime()) / 86400000.0,
            x2max = (service.axes.xmax.getTime() - service.date.getTime()) / 86400000.0,
            y2min = service.axes.y2min,
            y2max = service.axes.y2max;

        var xScale = d3.scaleUtc()
                        .domain([xmin, xmax])
                        .range([0, width]),
            x2Scale = d3.scaleLinear()
                        .domain([x2min, x2max])
                        .range([0, width]),
            yScale = d3.scaleLinear()
                        .domain([ymin, ymax])
                        .range([height - separator, 0]),
            y2Scale = d3.scaleLinear()
                        .domain([y2min, y2max])
                        .range([height, height - separator]);

        var xAxis_bottom = d3.axisBottom(xScale).ticks(6).tickFormat(d3.timeFormat('%H:00')),
            xAxis_seperator = d3.axisBottom(xScale).ticks(6).tickFormat(''),
            x2Axis_top = d3.axisTop(x2Scale),
            yAxis_left = d3.axisLeft(yScale),
            yAxis_right = d3.axisRight(yScale).tickFormat(''),
            y2Axis_left = d3.axisLeft(y2Scale).ticks(4),
            y2Axis_right = d3.axisRight(y2Scale).ticks(4).tickFormat('');

        var x = {};
        angular.forEach(['sunset', 'sunrise', 'civil_dusk', 'civil_dawn', 'nautical_dusk', 'nautical_dawn', 'astronomical_dusk', 'astronomical_dawn', 'nadir'], function (key) {
            if (angular.isDefined(service.night[key]) && service.night[key] !== null ) {
                x[key] = xScale(new Date(service.night[key]));
            }
        });

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

        if (angular.isDefined(x.sunset) && angular.isDefined(x.sunrise)) {
        area.append('g').append('rect')
            .attr("x", x.sunset)
            .attr("y", 0)
            .attr("width", x.sunrise - x.sunset)
            .attr("height", height)
            .attr('class', 'civil-twilight');
        }
        if (angular.isDefined(x.civil_dusk) && angular.isDefined(x.civil_dawn)) {
        area.append('g').append('rect')
            .attr("x", x.civil_dusk)
            .attr("y", 0)
            .attr("width", x.civil_dawn - x.civil_dusk)
            .attr("height", height)
            .attr('class', 'nautical-twilight');
        }
        if (angular.isDefined(x.nautical_dusk) && angular.isDefined(x.nautical_dawn)) {
            area.append('g').append('rect')
                .attr("x", x.nautical_dusk)
                .attr("y", 0)
                .attr("width", x.nautical_dawn - x.nautical_dusk)
                .attr("height", height)
                .attr('class', 'astronomical-twilight');
        }
        if (angular.isDefined(x.astronomical_dusk) && angular.isDefined(x.astronomical_dawn)) {
            area.append('g').append('rect')
                .attr("x", x.astronomical_dusk)
                .attr("y", 0)
                .attr("width", x.astronomical_dawn - x.astronomical_dusk)
                .attr("height", height)
                .attr('class', 'night');
        }

        plot.append('g').call(xAxis_bottom)
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + height + ')');
        plot.append('g').call(xAxis_seperator)
            .attr('class', 'axis')
            .attr('transform', 'translate(0,' + (height - separator) + ')');
        plot.append('g').call(x2Axis_top)
            .attr('class', 'axis')
            .attr('transform', 'translate(0,0)');

        plot.append('g').call(yAxis_left)
            .attr('class', 'axis')
            .attr('transform', 'translate(0, 0)');
        plot.append('g').call(yAxis_right)
            .attr('class', 'axis')
            .attr('transform', 'translate(' + width + ', 0)');

        plot.append('g').call(y2Axis_left)
            .attr('class', 'axis')
            .attr('transform', 'translate(0, 0)');
        plot.append('g').call(y2Axis_right)
            .attr('class', 'axis')
            .attr('transform', 'translate(' + width + ', 0)');

        // x labels
        plot.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(" + (width/2) +"," + (height+40) + ")")
            .attr('class', 'axis')
            .text("Zeit t");
        plot.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(" + (width/2) +",-30)")
            .attr('class', 'axis')
            .text('MJD (' + service.night.mjd + ')');

        // y labels
        plot.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(-40," + ((height - separator)/2) + ")rotate(-90)")
            .attr('class', 'axis')
            .text("Helligkeit m [Mag]");
        plot.append('g').append("text")
            .attr("text-anchor", "middle")
            .attr("transform", "translate(-40," + ((height - separator) + (separator)/2) + ")rotate(-90)")
            .attr('class', 'axis')
            .text('Höhe des Mondes');

        var line = d3.line()
            .x(function (d) { return xScale(new Date(d.timestamp)); })
            .y(function (d) { return yScale(d['magnitude']); });

        var line2 = d3.line()
            .x(function (d) { return xScale(new Date(d.timestamp)); })
            .y(function (d) { return y2Scale(d['altitude']); });

        area.append('g').append("path")
            .attr("d", line(service.measurements))
            .attr('class', 'data');

        area.append('g').append("path")
            .attr("d", line2(service.moonpositions))
            .attr('class', 'data');
    };

    plot_service.drawMonth = function(service, callback) {

        var margin = {top: 5, right: 5, bottom: 5, left: 5},
            width = 926 - margin.left - margin.right,
            height = 694.5 - margin.top - margin.bottom,
            night_margin = 5,
            night_width = (width - 6 * night_margin) / 7.0,
            night_height = (height - 5 * night_margin) / 6.0;

        var plot = d3.select('#plot-month')
            .append("g")
            .attr('class', 'month')
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        var week_offset = 0;

        var g = plot.selectAll('g').data(service.nights).enter()
            .append('g')
            .attr('class', 'night')
            .attr("transform", function(night) {
                var date = new Date(night.date);

                var weekday = date.getDay() - 1;
                if (weekday === -1) weekday = 6;

                // workaround if the first of the month is a monday
                if (date.getDate() === 1 && weekday === 0) {
                    week_offset = -1;
                }

                var week = week_offset + Math.ceil((date.getDate() - weekday) / 7);

                var offset_x = (night_width + night_margin) * weekday,
                    offset_y = (night_height + night_margin) * week;
                return "translate(" + offset_x + "," + offset_y + ")";
            })
            .on('click', callback);

        g.append('defs').append('clipPath')
            .attr('id', function(night) {
                return 'clip' + night.id;
            })
            .append('rect')
            .attr('x', '0')
            .attr('y', '0')
            .attr('width', night_width)
            .attr('height', night_height);


        g.append('rect')
            .attr('x', '0')
            .attr('y', '0')
            .attr('width', night_width)
            .attr('height', night_height);

        g.append('text')
            .attr('x', 5)
            .attr('y', 15)
            .text(function(night) {
                return $filter('date')(night.date);
            });

        g.append('g').append("path")
            .attr('class', 'data')
            .attr('clip-path', function(night) {
                return 'url(' + $window.location.href + '#clip' + night.id + ')';
            })
            .attr("d", function(night) {
                if (angular.isDefined(night.measurements) && night.measurements.length > 0) {
                    var date = new Date(night.date);
                    var xmin = new Date(date.getFullYear(), date.getMonth(), date.getDate(), 15),
                        xmax = new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1, 9);

                    var xScale = d3.scaleUtc().domain([xmin, xmax]).range([0, night_width]),
                        yScale = d3.scaleLinear().domain([22, 4]).range([night_height, 0]);

                    var line = d3.line()
                        .x(function (d) { return xScale(new Date(d.timestamp)); })
                        .y(function (d) { return yScale(d['magnitude']); });

                    return line(night.measurements);
                } else {
                    return '';
                }
            });
    };

    return plot_service;
}]);
