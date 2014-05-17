(function() {

    var module = angular.module('protips');

    module.directive('markdown', function () {
    var converter = new Showdown.converter();
    return {
        restrict: 'A',
        link: function (scope, element, attrs) {
            var htmlText = converter.makeHtml(element.text());
            element.html(htmlText);
        }
    };
    });

    module.controller('TipsCtrl', function($scope, api) {

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

        $scope.init = function() {
            $scope.fetchTips();
        };

        $scope.init();

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