(function() {

    var module = angular.module('protips');

    module.controller('TipsCtrl', function($scope, $modal, api) {

        $scope.currentPage = 1;
        $scope.tips = [];
        $scope.allTipsLoaded = false;
        $scope.loading = false;

        $scope.fetchTips = function() {
            if (!$scope.loading) {
                var params = {
                    page: $scope.currentPage
                };
                $scope.loading = true;
                api.fetch("/tips/", params, function(tips) {
                    $scope.tips = $scope.tips.concat(tips.results);
                    $scope.loading = false;
                    if ($scope.tips.length == tips.count) {
                        $scope.allTipsLoaded = true;
                    }
                });
            }
        };

        $scope.loadMoreTips = function() {
            $scope.currentPage += 1;
            $scope.fetchTips();
        };

        $scope.showDetails = function(tip) {
            var modalInstance = $modal.open({
                templateUrl: '/static/templates/tip_modal.html',
                controller: "TipModalCtrl",
                resolve: {
                    tip: function () {
                        return tip;
                    }
                }
            });
        };

        $scope.init = function() {
            $scope.fetchTips();
        };

        $scope.init();

    });

    module.controller('TipModalCtrl', function($scope, $modalInstance, tip) {

        $scope.tip = tip;

        $scope.dismiss = function() {
            $modalInstance.dismiss('close');
        };

    });

    module.controller('AddTipCtrl', function($scope, api) {

        $scope.errors = [];

        $scope.loading = false;

        $scope.tip = {
            description: "",
            title: "",
            language: 1,
            user: 1,
            created: "2014-01-01T12:00"
        }

        $scope.addTip = function() {
            $scope.loading = true;
            $scope.errors = [];
            api.post("/tips/logged/", $scope.tip,
                function(response, status, headers) {
                    var modal = $('#tip_modal');
                    modal.modal('hide');
                    $scope.$parent.tips.push($scope.tip);
                }, function(error) {
                    $scope.error = true;
                    $scope.loading = false;
                    $scope.errors = ["Unexpected error occurred."];
                });
        };

    });

})()