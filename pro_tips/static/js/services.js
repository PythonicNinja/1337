(function() {

    var module = angular.module('protips');

    module.service('api', function($http) {

        this.genericError = function(error) {
            alert("Unexpected error occurred. Please try again in a moment.")
        };

        this.fetch = function(url, params, callback, error) {
            $http({
                url: "/api" + url,
                method: "GET",
                params: params
            }).success(callback).error(error || this.genericError);
        };

        this.post = function(url, data, callback, error, captcha) {
            var config = {
                url: "/api" + url,
                headers: { 'Content-Type': data ? 'application/json' : 'text/plain' },
                method: "POST",
                data: data
            };
            $http(config).success(callback).error(error || this.genericError);
        };

        this.del = function(url, data, callback, error) {
            $http({
                url: "/api" + url,
                headers: { 'Content-Type': data ? 'application/json' : 'text/plain' },
                method: "DELETE",
                data: data
            }).success(callback).error(error || this.genericError);
        };

    });

})();