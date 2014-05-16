(function() {

    var module = angular.module('protips');

    module.controller('AddTipCtrl', function($scope, api) {

        $scope.errors = [];

        $scope.loading = false;

        $scope.tip = {
            contents: ""
        }

        $scope.addTip = function() {
            $scope.loading = true;
            $scope.errors = [];
            api.post("/tip", $scope.tip,
                function(response, status, headers) {
                    var modal = $('#tip_modal');
                    modal.modal('hide');
                }, function(error) {
                    $scope.error = true;
                    $scope.loading = false;
                    $scope.errors = ["Unexpected error occurred."];
                });
        };

    });

})()