app.controller('DataController', ['$scope','DataService',function($scope, DataService) {

    $scope.service = DataService;
    $scope.service.init();

}]);
