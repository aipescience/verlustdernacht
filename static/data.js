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

        if (date.getHours() > 12) {
            date.setDate(date.getDate() - 1);
        }
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
        });
    }

    service.init = function() {

        service.date = getDate(); new Date();
        fetchLocations();

    };

    return service;
}]);

app.controller('DataController', ['$scope','DataService',function($scope, DataService) {

    $scope.service = DataService;
    $scope.service.init();

}]);
