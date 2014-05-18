(function() {

    var module = angular.module('protips');

    module.directive('markdown', function ($compile) {
        var converter = new Showdown.converter();
        return {
            restrict: 'A',
            link: function (scope, element, attrs) {
                var htmlText = converter.makeHtml(element.text());
                element.html($compile(htmlText)(scope));
            }
        };
    });

})()