angular.module('MainApp.directives', [])
  .directive('myMinlength', [function () {
    return {
        require: 'ngModel'
      , restrict: 'A'
      , link: function (scope, elem, attrs, ctrl) {
          function minlength (val) {
            ctrl.$setValidity('myMinlength', val && )
            ctrl.$render()
          }

          ctrl.$parsers.push(minlength)
        }
    }
  }])