app = angular.module('data',['ngResource'])

.config(['$httpProvider', '$interpolateProvider', '$locationProvider', '$resourceProvider', function($httpProvider, $interpolateProvider, $locationProvider, $resourceProvider) {
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
}])

.controller('DataController', ['$scope','DataService',function($scope, DataService) {

    $scope.service = DataService;
    $scope.service.init();

}]);
