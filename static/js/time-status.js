var app = angular.module("timeStatus", ['nvd3ChartDirectives']);

app.controller('bulletChartController', function($scope, $http) {
    var convertSecondsToHours = function(seconds) {
        return (seconds/60.0/60).toFixed(2);
    }


    var getUrl = function(period, category) {
        return 'api/time-series?period=' + period + '&category=' + category;
    }

    $scope.screenData = {};

    $http.get(getUrl('1m', 'Screen'))
        .then(function(response) {
            var period1Seconds = 0;
            response.data.times.forEach(function(time) {
                period1Seconds += time.seconds;
            });
            var period1Hours = convertSecondsToHours(period1Seconds);
            $scope.screenData["measures"] = [period1Hours];
            $http.get(getUrl('2m', 'Screen'))
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

    $scope.gymData = {};

    $http.get(getUrl('1m', 'Gym'))
        .then(function(response) {
            var period1Seconds = 0;
            response.data.times.forEach(function(time) {
                period1Seconds += time.seconds;
            });
            var period1Hours = convertSecondsToHours(period1Seconds);
            $scope.gymData["measures"] = [period1Hours];
            $http.get(getUrl('2m', 'Gym'))
                .then(function(response) {
                    var period2Seconds = 0;
                    response.data.times.forEach(function(time) {
                        period2Seconds += time.seconds;
                    });
                    period2Seconds = period2Seconds - period1Seconds;
                    var period2Hours = convertSecondsToHours(period2Seconds);
                    var maxRange = Math.max(period1Hours, period2Hours) * 1.1;
                    $scope.gymData = {
                        "title": "Gym Data",
                        "subtitle": "Measured in hours",
                        "ranges": [0, maxRange],
                        "markers": [period2Hours],
                        "measures": [period1Hours]
                    };
                });
        });

    $scope.workData = {};

    $http.get(getUrl('1m', 'Work'))
        .then(function(response) {
            var period1Seconds = 0;
            response.data.times.forEach(function(time) {
                period1Seconds += time.seconds;
            });
            var period1Hours = convertSecondsToHours(period1Seconds);
            $scope.workData["measures"] = [period1Hours];
            $http.get(getUrl('2m', 'Work'))
                .then(function(response) {
                    var period2Seconds = 0;
                    response.data.times.forEach(function(time) {
                        period2Seconds += time.seconds;
                    });
                    period2Seconds = period2Seconds - period1Seconds;
                    var period2Hours = convertSecondsToHours(period2Seconds);
                    var maxRange = Math.max(period1Hours, period2Hours) * 1.1;
                    $scope.workData = {
                        "title": "Work Data",
                        "subtitle": "Measured in hours",
                        "ranges": [0, maxRange],
                        "markers": [period2Hours],
                        "measures": [period1Hours]
                    };
                });
        });

    $scope.drivingData = {};

    $http.get(getUrl('1m', 'Driving'))
        .then(function(response) {
            var period1Seconds = 0;
            response.data.times.forEach(function(time) {
                period1Seconds += time.seconds;
            });
            var period1Hours = convertSecondsToHours(period1Seconds);
            $scope.drivingData["measures"] = [period1Hours];
            $http.get(getUrl('2m', 'Driving'))
                .then(function(response) {
                    var period2Seconds = 0;
                    response.data.times.forEach(function(time) {
                        period2Seconds += time.seconds;
                    });
                    period2Seconds = period2Seconds - period1Seconds;
                    var period2Hours = convertSecondsToHours(period2Seconds);
                    var maxRange = Math.max(period1Hours, period2Hours) * 1.1;
                    $scope.drivingData = {
                        "title": "Driving Data",
                        "subtitle": "Measured in hours",
                        "ranges": [0, maxRange],
                        "markers": [period2Hours],
                        "measures": [period1Hours]
                    };
                });
        });

    $scope.sportrockData = {};

    $http.get(getUrl('1m', 'Sportrock'))
        .then(function(response) {
            var period1Seconds = 0;
            response.data.times.forEach(function(time) {
                period1Seconds += time.seconds;
            });
            var period1Hours = convertSecondsToHours(period1Seconds);
            $scope.sportrockData["measures"] = [period1Hours];
            $http.get(getUrl('2m', 'Sportrock'))
                .then(function(response) {
                    var period2Seconds = 0;
                    response.data.times.forEach(function(time) {
                        period2Seconds += time.seconds;
                    });
                    period2Seconds = period2Seconds - period1Seconds;
                    var period2Hours = convertSecondsToHours(period2Seconds);
                    var maxRange = Math.max(period1Hours, period2Hours) * 1.1;
                    $scope.sportrockData = {
                        "title": "Sportrock Data",
                        "subtitle": "Measured in hours",
                        "ranges": [0, maxRange],
                        "markers": [period2Hours],
                        "measures": [period1Hours]
                    };
                });
        });

    $scope.homeData = {};

    $http.get(getUrl('1m', 'Home'))
        .then(function(response) {
            var period1Seconds = 0;
            response.data.times.forEach(function(time) {
                period1Seconds += time.seconds;
            });
            var period1Hours = convertSecondsToHours(period1Seconds);
            $scope.homeData["measures"] = [period1Hours];
            $http.get(getUrl('2m', 'Home'))
                .then(function(response) {
                    var period2Seconds = 0;
                    response.data.times.forEach(function(time) {
                        period2Seconds += time.seconds;
                    });
                    period2Seconds = period2Seconds - period1Seconds;
                    var period2Hours = convertSecondsToHours(period2Seconds);
                    var maxRange = Math.max(period1Hours, period2Hours) * 1.1;
                    $scope.homeData = {
                        "title": "Home Data",
                        "subtitle": "Measured in hours",
                        "ranges": [0, maxRange],
                        "markers": [period2Hours],
                        "measures": [period1Hours]
                    };
                });
        });
});
