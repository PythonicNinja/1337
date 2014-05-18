(function() {

    var module = angular.module('protips');

    module.controller('TipsCtrl', function($scope, $rootScope, $modal, api) {


        $scope.initialize = function (is_authenticated, user_id) {
            $scope.is_authenticated = is_authenticated;
            $scope.user_id = user_id;
        };


        $scope.language = $rootScope.getURLParameter("language");

        $scope.currentPage = 1;
        $scope.tips = [];
        $scope.allTipsLoaded = false;
        $scope.loading = false;

        $scope.fetchTips = function() {
            if (!$scope.loading) {
                var params = {
                    page: $scope.currentPage
                };
                if ($scope.language) {
                    params['language'] = $scope.language;
                }
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

        $scope.addToFav = function(tip) {
            api.post("/tip/favourites/logged/", {tip: tip.id, user: $scope.user_id}, function(result) {
                alert("Fav added");
            }, function(err) {
                alert("Error adding fav: " + err);
            });
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

    module.controller('TipModalCtrl', function($scope, $modalInstance, api, tip) {

        $scope.tip = tip;

        $scope.voteUp = function() {
            $scope.vote(true);
        };

        $scope.voteDown = function() {
            $scope.vote(false);
        };

        $scope.vote = function(voteType) {
            api.post("/tips/votes/logged/", {tip: tip.id, user: $scope.user_id, 'type': voteType}, function(result) {
                alert("Vote added");
            }, function(err) {
                alert("Error adding vote: " + err);
            });
        };

        $scope.dismiss = function() {
            $modalInstance.dismiss('close');
        };

    });

    module.controller('TipCommentsCtrl', function($scope, api) {

        $scope.comment = "";

        $scope.comments = [];

        $scope.fetchComments = function() {
            api.fetch("/tip/comments/", {id: $scope.$parent.tip.id}, function(comments) {
                $scope.comments = comments;
            });
        };

        $scope.addComment = function() {
            api.post("/comment/add/", {tip_id: $scope.$parent.tip.id, comment_text: $scope.comment}, function() {
                $scope.comment = "";
                $scope.fetchComments();
            });
        };

        $scope.init = function() {
            $scope.fetchComments();
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