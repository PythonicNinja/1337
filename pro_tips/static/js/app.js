(function () {

    var module = angular.module('protips', []);

    module.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });

    module.run(function() {
    });

})();
