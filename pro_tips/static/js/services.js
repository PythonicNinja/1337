(function() {

    var module = angular.module('protips');

    module.service('api', function($http) {

        this.getCookie = function(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        };

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
                headers: {
                    'Content-Type': data ? 'application/json' : 'text/plain',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                method: "POST",
                data: data
            };
            $http(config).success(callback).error(error || this.genericError);
        };

        this.del = function(url, data, callback, error) {
            $http({
                url: "/api" + url,
                headers: {
                    'Content-Type': data ? 'application/json' : 'text/plain',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                method: "DELETE",
                data: data
            }).success(callback).error(error || this.genericError);
        };

    });

})();