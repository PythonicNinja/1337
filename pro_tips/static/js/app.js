(function () {

    var module = angular.module('protips', ['ui.bootstrap']);

    module.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });

    module.run(function($rootScope) {

        $rootScope.getURLParameter = function(name) {
            return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
        };

    });

})();
