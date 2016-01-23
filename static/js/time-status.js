var app = angular.module("timeStatus", ['nvd3ChartDirectives']);

app.controller('bulletChartController', function($scope, $http) {
    $scope.screenData = {};

    $http.get('api/time-series?period=1m&category=Screen')
        .then(function(response) {
            var period1Seconds = 0;
            response.data.times.forEach(function(time) {
                period1Seconds += time.seconds;
            });
            var period1Hours = convertSecondsToHours(period1Seconds);
            $scope.screenData["measures"] = [period1Hours];
            $http.get('api/time-series?period=2m&category=Screen')
                .then(function(response) {
                    var period2Seconds = 0;
                    response.data.times.forEach(function(time) {
                        period2Seconds += time.seconds;
                    });
                    period2Seconds = period2Seconds - period1Seconds;
                    var period2Hours = convertSecondsToHours(period2Seconds);
                    var maxRange = Math.max(period1Hours, period2Hours) * 1.1;
                    $scope.screenData = {
                        "title": "Screen Data",
                        "subtitle": "Measured in hours",
                        "ranges": [0, maxRange],
                        "markers": [period2Hours],
                        "measures": [period1Hours]
                    };
                });
        });

    var convertSecondsToHours = function(seconds) {
        return seconds/60.0/60;
    }
});
