var app = angular.module("timeStatus", ['nvd3ChartDirectives']);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);

app.controller('bulletChartController', function($scope, $http) {
    var convertSecondsToHours = function(seconds) {
        return (seconds/60.0/60).toFixed(2);
    }

    $scope.screenData = {};
    $scope.gymData = {};
    $scope.sportrockData = {};
    $scope.workData = {};
    $scope.homeData = {};
    $scope.drivingData = {};

    var getBulletData = function(data, category) {
        var bulletData = data[category]
        var maxRange = Math.max(bulletData['previous'],
                                bulletData['current']) * 1.1;
        return {
            "title": category + " Data",
            "subtitle": "Measured in hours",
            "ranges": [0, maxRange],
            "markers": [bulletData['previous']],
            "measures": [bulletData['current']]
        };
    };

    $http.get('api/time-series/month?category=Screen' +
              '&category=Gym&category=Work&category=Sportrock' +
              '&category=Driving&category=Home')
        .then(function(response) {
            var data = response.data;

            $scope.screenData = getBulletData(data, 'Screen');
            $scope.gymData = getBulletData(data, 'Gym');
            $scope.sportrockData = getBulletData(data, 'Sportrock');
            $scope.workData = getBulletData(data, 'Work');
            $scope.homeData = getBulletData(data, 'Home');
            $scope.drivingData = getBulletData(data, 'Driving');

            $scope.latest_date = new Date(data['period']['end_date']['$date'])
                .toLocaleDateString();
            $scope.period2_date = new Date(
                data['period']['period2_start_date']['$date'])
                .toLocaleDateString();
            $scope.period_date = new Date(data['period']['period_start_date']['$date'])
                .toLocaleDateString();
        });
});
