(function () {

    var module = angular.module('protips', ['ui.bootstrap']);

    module.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });

    module.run(function() {
    });

})();
