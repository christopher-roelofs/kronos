angular.module('MainApp', ['MainApp.controllers', 'MainApp.directives'])
  .run(['$rootScope', function ($rootScope) {
    $rootScope.$scopeExtend = function (obj, cb) {
      $rootScope = angular.extend($rootScope, obj)

      if (cb) {
        cb()
      }
    }
  }])
