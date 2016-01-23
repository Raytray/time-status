var app = angular.module("timeStatus", ['nvd3ChartDirectives']);

app.controller('bulletChartController', function($scope, $http) {
    $scope.screenData = {};

    $http.get('api/time-series?period=1m&category=Screen')
        .then(function(response) {
            total = 0;
            response.data.times.forEach(function(time) {
                total += time.seconds;
            });
            total = total / 60.0 / 24;
            console.log(total);
            $scope.screenData = {
                "measures": [total],
                "title": "Screen Data",
                "subtitle": "Measured in hours",
                "ranges": [0, 500]
            };
        });
});
