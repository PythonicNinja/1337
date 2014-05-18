(function() {

    var module = angular.module('protips');

    module.directive('markdown', function ($compile) {
        var converter = new Showdown.converter();
        return {
            restrict: 'A',
            link: function (scope, element, attrs) {
                element.html(converter.makeHtml(scope.tip.description));
            }
        };
    });

})()