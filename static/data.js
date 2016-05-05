app = angular.module('data',[]);

app.factory('DataService', ['$http','$window',function($http,$window) {

    var values = {};
    var errors = {};

    return {
        values: values,
        errors: errors,
        // fetchHtml: function (url) {
        //     $http.get(url,{'headers': {'Accept': 'application/html'}}).success(function(html) {
        //         for (var value in values) delete values[value];
        //         for (var error in errors) delete errors[error];

        //         if (ModalService.modal.html != html) {
        //             ModalService.modal.html = html;
        //         }

        //         activeUrl = url;
        //         ModalService.modal.enabled = true;
        //     });
        // },
        // submitForm: function(submit) {
        //     if (submit) {
        //         var data = {
        //             'csrf': angular.element('#csrf').attr('value')
        //         };

        //         // merge with form values and take arrays into account
        //         angular.forEach(values, function(value, key) {
        //             if (angular.isObject(value)) {
        //                 data[key] = [];

        //                 if (angular.isArray(value)) {
        //                     // this is an array coming from a multiselect
        //                     angular.forEach(value, function(v,k) {
        //                         data[key].push(v);
        //                     });
        //                 } else {
        //                     // this is an object coming from a set of checkboxes
        //                     angular.forEach(value, function(v,k) {
        //                         if (v === true) {
        //                             // for value from a set of checkboxes use the key
        //                             data[key].push(k);
        //                         }
        //                     });
        //                 }
        //             } else {
        //                 data[key] = value;
        //             }
        //         });

        //         // fire up post request
        //         $http.post(activeUrl,$.param(data)).success(function(response) {
        //             for (var error in errors) delete errors[error];

        //             if (response.status === 'ok') {
        //                 ModalService.modal.enabled = false;

        //                 if (table) {
        //                     TableService.fetchRows();
        //                 } else {
        //                     $window.location.reload();
        //                 }
        //             } else if (response.status === 'error') {
        //                 angular.forEach(response.errors, function(error, key) {
        //                     errors[key] = error;
        //                 });
        //             } else {
        //                 errors['form'] = {'form': 'Error: Unknown response from server.'};
        //             }
        //         });
        //     } else {
        //         ModalService.modal.enabled = false;
        //     }
        // }
    };
}]);

app.controller('DataController', ['$scope','DataService',function($scope,DataService) {

    $scope.values = DataService.values;
    $scope.errors = DataService.errors;

    // $scope.fetchHtml = function(event) {
    //     DataService.fetchHtml(event.target.href);
    //     event.preventDefault();
    // };

    // $scope.submitForm = function() {
    //     DataService.submitForm($scope.submit);
    // };
}]);