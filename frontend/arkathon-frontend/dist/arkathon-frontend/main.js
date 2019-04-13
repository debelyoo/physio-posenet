(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ "./src/$$_lazy_route_resource lazy recursive":
/*!**********************************************************!*\
  !*** ./src/$$_lazy_route_resource lazy namespace object ***!
  \**********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error("Cannot find module '" + req + "'");
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "./src/$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "./src/app/app-routing.module.ts":
/*!***************************************!*\
  !*** ./src/app/app-routing.module.ts ***!
  \***************************************/
/*! exports provided: AppRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() { return AppRoutingModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _capture_camera_capture_camera_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./capture-camera/capture-camera.component */ "./src/app/capture-camera/capture-camera.component.ts");
/* harmony import */ var _patient_patient_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./patient/patient.component */ "./src/app/patient/patient.component.ts");
/* harmony import */ var _exercise_exercise_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./exercise/exercise.component */ "./src/app/exercise/exercise.component.ts");
/* harmony import */ var _electrodes_electrodes_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./electrodes/electrodes.component */ "./src/app/electrodes/electrodes.component.ts");
/* harmony import */ var _doctor_view_doctor_view_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./doctor-view/doctor-view.component */ "./src/app/doctor-view/doctor-view.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};







var routes = [
    { path: 'patient', component: _patient_patient_component__WEBPACK_IMPORTED_MODULE_3__["PatientComponent"] },
    { path: 'exercise/:id', component: _exercise_exercise_component__WEBPACK_IMPORTED_MODULE_4__["ExerciseComponent"] },
    { path: 'record', component: _capture_camera_capture_camera_component__WEBPACK_IMPORTED_MODULE_2__["CaptureCameraComponent"] },
    { path: 'electrodes', component: _electrodes_electrodes_component__WEBPACK_IMPORTED_MODULE_5__["ElectrodesComponent"] },
    { path: 'doctor', component: _doctor_view_doctor_view_component__WEBPACK_IMPORTED_MODULE_6__["DoctorViewComponent"] },
];
var AppRoutingModule = /** @class */ (function () {
    function AppRoutingModule() {
    }
    AppRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"].forRoot(routes)],
            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"]]
        })
    ], AppRoutingModule);
    return AppRoutingModule;
}());



/***/ }),

/***/ "./src/app/app.component.css":
/*!***********************************!*\
  !*** ./src/app/app.component.css ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "button {\n    margin-right: 8px;\n}\n\nmat-toolbar {\n    background-color: #B3E5FC;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvYXBwLmNvbXBvbmVudC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7SUFDSSxrQkFBa0I7Q0FDckI7O0FBRUQ7SUFDSSwwQkFBMEI7Q0FDN0IiLCJmaWxlIjoic3JjL2FwcC9hcHAuY29tcG9uZW50LmNzcyIsInNvdXJjZXNDb250ZW50IjpbImJ1dHRvbiB7XG4gICAgbWFyZ2luLXJpZ2h0OiA4cHg7XG59XG5cbm1hdC10b29sYmFyIHtcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjQjNFNUZDO1xufSJdfQ== */"

/***/ }),

/***/ "./src/app/app.component.html":
/*!************************************!*\
  !*** ./src/app/app.component.html ***!
  \************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<mat-toolbar>\n    <mat-toolbar-row>\n        <div>\n            <button mat-button (click)=\"goBack()\">Back</button>\n        </div>\n        <div class=\"nav-button-row\">\n          <button mat-raised-button (click)=\"openDoctorPage()\">Doctor</button>\n          <button mat-raised-button (click)=\"openPatientPage()\">Patient</button>\n        </div>\n    </mat-toolbar-row>\n  </mat-toolbar>\n<main>\n  <router-outlet></router-outlet>\n</main>"

/***/ }),

/***/ "./src/app/app.component.ts":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var AppComponent = /** @class */ (function () {
    function AppComponent(router, _location) {
        this.router = router;
        this._location = _location;
    }
    AppComponent.prototype.openPatientPage = function () {
        this.router.navigate(['patient']);
    };
    AppComponent.prototype.openDoctorPage = function () {
        this.router.navigate(['doctor']);
    };
    AppComponent.prototype.goBack = function () {
        this._location.back();
    };
    AppComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-root',
            template: __webpack_require__(/*! ./app.component.html */ "./src/app/app.component.html"),
            styles: [__webpack_require__(/*! ./app.component.css */ "./src/app/app.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"],
            _angular_common__WEBPACK_IMPORTED_MODULE_2__["Location"]])
    ], AppComponent);
    return AppComponent;
}());



/***/ }),

/***/ "./src/app/app.module.ts":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/fesm5/platform-browser.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _app_routing_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app-routing.module */ "./src/app/app-routing.module.ts");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./app.component */ "./src/app/app.component.ts");
/* harmony import */ var _angular_material__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/material */ "./node_modules/@angular/material/esm5/material.es5.js");
/* harmony import */ var _angular_material_card__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/material/card */ "./node_modules/@angular/material/esm5/card.es5.js");
/* harmony import */ var _capture_camera_capture_camera_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./capture-camera/capture-camera.component */ "./src/app/capture-camera/capture-camera.component.ts");
/* harmony import */ var _patient_patient_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./patient/patient.component */ "./src/app/patient/patient.component.ts");
/* harmony import */ var _services_backend_service_service__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./services/backend-service.service */ "./src/app/services/backend-service.service.ts");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
/* harmony import */ var _exercise_exercise_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./exercise/exercise.component */ "./src/app/exercise/exercise.component.ts");
/* harmony import */ var _angular_material_progress_bar__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @angular/material/progress-bar */ "./node_modules/@angular/material/esm5/progress-bar.es5.js");
/* harmony import */ var _exercise_table_exercise_table_component__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./exercise-table/exercise-table.component */ "./src/app/exercise-table/exercise-table.component.ts");
/* harmony import */ var _angular_material_table__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @angular/material/table */ "./node_modules/@angular/material/esm5/table.es5.js");
/* harmony import */ var _electrodes_electrodes_component__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ./electrodes/electrodes.component */ "./src/app/electrodes/electrodes.component.ts");
/* harmony import */ var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @angular/material/toolbar */ "./node_modules/@angular/material/esm5/toolbar.es5.js");
/* harmony import */ var _doctor_view_doctor_view_component__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! ./doctor-view/doctor-view.component */ "./src/app/doctor-view/doctor-view.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};

















var AppModule = /** @class */ (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
            declarations: [
                _app_component__WEBPACK_IMPORTED_MODULE_3__["AppComponent"],
                _patient_patient_component__WEBPACK_IMPORTED_MODULE_7__["PatientComponent"],
                _capture_camera_capture_camera_component__WEBPACK_IMPORTED_MODULE_6__["CaptureCameraComponent"],
                _exercise_exercise_component__WEBPACK_IMPORTED_MODULE_10__["ExerciseComponent"],
                _exercise_table_exercise_table_component__WEBPACK_IMPORTED_MODULE_12__["ExerciseTableComponent"],
                _electrodes_electrodes_component__WEBPACK_IMPORTED_MODULE_14__["ElectrodesComponent"],
                _doctor_view_doctor_view_component__WEBPACK_IMPORTED_MODULE_16__["DoctorViewComponent"]
            ],
            imports: [
                _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
                _angular_common_http__WEBPACK_IMPORTED_MODULE_9__["HttpClientModule"],
                _app_routing_module__WEBPACK_IMPORTED_MODULE_2__["AppRoutingModule"],
                _angular_material__WEBPACK_IMPORTED_MODULE_4__["MatButtonModule"],
                _angular_material__WEBPACK_IMPORTED_MODULE_4__["MatCheckboxModule"],
                _angular_material_card__WEBPACK_IMPORTED_MODULE_5__["MatCardModule"],
                _angular_material_progress_bar__WEBPACK_IMPORTED_MODULE_11__["MatProgressBarModule"],
                _angular_material_table__WEBPACK_IMPORTED_MODULE_13__["MatTableModule"],
                _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_15__["MatToolbarModule"]
            ],
            providers: [_services_backend_service_service__WEBPACK_IMPORTED_MODULE_8__["BackendServiceService"]],
            bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_3__["AppComponent"]]
        })
    ], AppModule);
    return AppModule;
}());



/***/ }),

/***/ "./src/app/capture-camera/capture-camera.component.css":
/*!*************************************************************!*\
  !*** ./src/app/capture-camera/capture-camera.component.css ***!
  \*************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".mg-2 {\n margin: 2px;\n}\n\n.mg-6 {\n    margin: 6px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvY2FwdHVyZS1jYW1lcmEvY2FwdHVyZS1jYW1lcmEuY29tcG9uZW50LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtDQUNDLFlBQVk7Q0FDWjs7QUFFRDtJQUNJLFlBQVk7Q0FDZiIsImZpbGUiOiJzcmMvYXBwL2NhcHR1cmUtY2FtZXJhL2NhcHR1cmUtY2FtZXJhLmNvbXBvbmVudC5jc3MiLCJzb3VyY2VzQ29udGVudCI6WyIubWctMiB7XG4gbWFyZ2luOiAycHg7XG59XG5cbi5tZy02IHtcbiAgICBtYXJnaW46IDZweDtcbn0iXX0= */"

/***/ }),

/***/ "./src/app/capture-camera/capture-camera.component.html":
/*!**************************************************************!*\
  !*** ./src/app/capture-camera/capture-camera.component.html ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<video #videoElement></video>\n<div class=\"row\">\n  <button class=\"mg-2\" (click)=\"start()\" mat-raised-button>Play</button>\n  <button class=\"mg-2\" (click)=\"stop()\" mat-raised-button>Stop</button>\n</div>\n<div *ngIf=\"videoOn\">\n  <div class=\"mg-6\">\n    Progress:\n    <mat-progress-bar\n      class=\"example-margin\"\n      [color]=\"color\"\n      [mode]=\"mode\"\n      [value]=\"value\">\n    </mat-progress-bar>\n  </div>\n  <div class=\"mg-6\">\n    Time:\n    <label>{{tick}}</label>\n  </div> \n  <div class=\"mg-6\">\n    Count:\n    <label>{{count}}</label>\n  </div>\n</div>"

/***/ }),

/***/ "./src/app/capture-camera/capture-camera.component.ts":
/*!************************************************************!*\
  !*** ./src/app/capture-camera/capture-camera.component.ts ***!
  \************************************************************/
/*! exports provided: CaptureCameraComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CaptureCameraComponent", function() { return CaptureCameraComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var rxjs_internal_observable_timer__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! rxjs/internal/observable/timer */ "./node_modules/rxjs/internal/observable/timer.js");
/* harmony import */ var rxjs_internal_observable_timer__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(rxjs_internal_observable_timer__WEBPACK_IMPORTED_MODULE_1__);
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var source = Object(rxjs_internal_observable_timer__WEBPACK_IMPORTED_MODULE_1__["timer"])(1, 1000);
var CaptureCameraComponent = /** @class */ (function () {
    function CaptureCameraComponent() {
        this.videoOn = false;
        this.color = 'primary';
        this.mode = 'determinate';
        this.value = 0;
        this.tick = 0;
        this.countable = false;
        this.count = 0;
    }
    CaptureCameraComponent.prototype.ngOnInit = function () {
        this.video = this.videoElement.nativeElement;
    };
    CaptureCameraComponent.prototype.start = function () {
        this.countable = true;
        this.videoOn = true;
        this.initCamera({ video: true, audio: false });
        this.startTimer();
        this.value = 60;
        this.setRandomProgress();
    };
    CaptureCameraComponent.prototype.stop = function () {
        this.video.pause();
        this.pauseTimer();
        if (this.countable) {
            this.count++;
            this.countable = false;
        }
    };
    CaptureCameraComponent.prototype.initCamera = function (config) {
        var _this = this;
        var browser = navigator;
        browser.getUserMedia = (browser.getUserMedia ||
            browser.webkitGetUserMedia ||
            browser.mozGetUserMedia ||
            browser.msGetUserMedia);
        browser.mediaDevices.getUserMedia(config)
            .then(function (stream) {
            _this.video.srcObject = stream;
            _this.video.play();
        });
    };
    CaptureCameraComponent.prototype.startTimer = function () {
        var _this = this;
        this.timerSubscription = source.subscribe(function (tick) { return _this.tick = tick; });
    };
    CaptureCameraComponent.prototype.pauseTimer = function () {
        if (this.timerSubscription) {
            this.timerSubscription.unsubscribe();
        }
    };
    CaptureCameraComponent.prototype.setRandomProgress = function () {
        var _this = this;
        setInterval(function () {
            _this.value = Math.floor(Math.random() * 40) + 60;
        }, 1000);
    };
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ViewChild"])('videoElement'),
        __metadata("design:type", Object)
    ], CaptureCameraComponent.prototype, "videoElement", void 0);
    CaptureCameraComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-capture-camera',
            template: __webpack_require__(/*! ./capture-camera.component.html */ "./src/app/capture-camera/capture-camera.component.html"),
            styles: [__webpack_require__(/*! ./capture-camera.component.css */ "./src/app/capture-camera/capture-camera.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], CaptureCameraComponent);
    return CaptureCameraComponent;
}());



/***/ }),

/***/ "./src/app/doctor-view/doctor-view.component.css":
/*!*******************************************************!*\
  !*** ./src/app/doctor-view/doctor-view.component.css ***!
  \*******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "input[type=\"file\"] {\n    display: none;\n}\n\n.custom-file-upload {\n    cursor: pointer;\n\n    color: #fff !important;\n    text-transform: uppercase;\n    background: #3F51B5;\n    line-height: 36px;\n    margin: 6px;\n    padding: 0 16px;\n    border-radius: 5px;\n    display: inline-block;\n    border: none;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvZG9jdG9yLXZpZXcvZG9jdG9yLXZpZXcuY29tcG9uZW50LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtJQUNJLGNBQWM7Q0FDakI7O0FBRUQ7SUFDSSxnQkFBZ0I7O0lBRWhCLHVCQUF1QjtJQUN2QiwwQkFBMEI7SUFDMUIsb0JBQW9CO0lBQ3BCLGtCQUFrQjtJQUNsQixZQUFZO0lBQ1osZ0JBQWdCO0lBQ2hCLG1CQUFtQjtJQUNuQixzQkFBc0I7SUFDdEIsYUFBYTtDQUNoQiIsImZpbGUiOiJzcmMvYXBwL2RvY3Rvci12aWV3L2RvY3Rvci12aWV3LmNvbXBvbmVudC5jc3MiLCJzb3VyY2VzQ29udGVudCI6WyJpbnB1dFt0eXBlPVwiZmlsZVwiXSB7XG4gICAgZGlzcGxheTogbm9uZTtcbn1cblxuLmN1c3RvbS1maWxlLXVwbG9hZCB7XG4gICAgY3Vyc29yOiBwb2ludGVyO1xuXG4gICAgY29sb3I6ICNmZmYgIWltcG9ydGFudDtcbiAgICB0ZXh0LXRyYW5zZm9ybTogdXBwZXJjYXNlO1xuICAgIGJhY2tncm91bmQ6ICMzRjUxQjU7XG4gICAgbGluZS1oZWlnaHQ6IDM2cHg7XG4gICAgbWFyZ2luOiA2cHg7XG4gICAgcGFkZGluZzogMCAxNnB4O1xuICAgIGJvcmRlci1yYWRpdXM6IDVweDtcbiAgICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG4gICAgYm9yZGVyOiBub25lO1xufSJdfQ== */"

/***/ }),

/***/ "./src/app/doctor-view/doctor-view.component.html":
/*!********************************************************!*\
  !*** ./src/app/doctor-view/doctor-view.component.html ***!
  \********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<form>\n    <label for=\"myForm\" class=\"custom-file-upload\">\n        <input id=\"myForm\" type=\"file\" name=\"file\" (change)=\"uploadPose($event.target.files)\"> Upload Pose\n    </label>\n</form>"

/***/ }),

/***/ "./src/app/doctor-view/doctor-view.component.ts":
/*!******************************************************!*\
  !*** ./src/app/doctor-view/doctor-view.component.ts ***!
  \******************************************************/
/*! exports provided: DoctorViewComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "DoctorViewComponent", function() { return DoctorViewComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var DoctorViewComponent = /** @class */ (function () {
    function DoctorViewComponent(http) {
        this.http = http;
        this.URL = 'https://physio.test.sqooba.io/api/poses';
    }
    DoctorViewComponent.prototype.ngOnInit = function () {
    };
    DoctorViewComponent.prototype.uploadPose = function (files) {
        this.fileToUpload = files.item(0);
        var formData = new FormData();
        formData.append('file', this.fileToUpload, this.fileToUpload.name);
        this.http.post(this.URL, formData).subscribe(function (val) {
            console.log(val);
        });
        return false;
    };
    DoctorViewComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-doctor-view',
            template: __webpack_require__(/*! ./doctor-view.component.html */ "./src/app/doctor-view/doctor-view.component.html"),
            styles: [__webpack_require__(/*! ./doctor-view.component.css */ "./src/app/doctor-view/doctor-view.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"]])
    ], DoctorViewComponent);
    return DoctorViewComponent;
}());



/***/ }),

/***/ "./src/app/electrodes/electrodes.component.css":
/*!*****************************************************!*\
  !*** ./src/app/electrodes/electrodes.component.css ***!
  \*****************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2VsZWN0cm9kZXMvZWxlY3Ryb2Rlcy5jb21wb25lbnQuY3NzIn0= */"

/***/ }),

/***/ "./src/app/electrodes/electrodes.component.html":
/*!******************************************************!*\
  !*** ./src/app/electrodes/electrodes.component.html ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<!-- Needs to be replced with HTML for setting electrodes -->\n<app-capture-camera></app-capture-camera>"

/***/ }),

/***/ "./src/app/electrodes/electrodes.component.ts":
/*!****************************************************!*\
  !*** ./src/app/electrodes/electrodes.component.ts ***!
  \****************************************************/
/*! exports provided: ElectrodesComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ElectrodesComponent", function() { return ElectrodesComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var ElectrodesComponent = /** @class */ (function () {
    function ElectrodesComponent() {
    }
    ElectrodesComponent.prototype.ngOnInit = function () {
    };
    ElectrodesComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-electrodes',
            template: __webpack_require__(/*! ./electrodes.component.html */ "./src/app/electrodes/electrodes.component.html"),
            styles: [__webpack_require__(/*! ./electrodes.component.css */ "./src/app/electrodes/electrodes.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], ElectrodesComponent);
    return ElectrodesComponent;
}());



/***/ }),

/***/ "./src/app/exercise-table/exercise-table.component.css":
/*!*************************************************************!*\
  !*** ./src/app/exercise-table/exercise-table.component.css ***!
  \*************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "table {\n    margin: 3px;\n    width: 100%;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvZXhlcmNpc2UtdGFibGUvZXhlcmNpc2UtdGFibGUuY29tcG9uZW50LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtJQUNJLFlBQVk7SUFDWixZQUFZO0NBQ2YiLCJmaWxlIjoic3JjL2FwcC9leGVyY2lzZS10YWJsZS9leGVyY2lzZS10YWJsZS5jb21wb25lbnQuY3NzIiwic291cmNlc0NvbnRlbnQiOlsidGFibGUge1xuICAgIG1hcmdpbjogM3B4O1xuICAgIHdpZHRoOiAxMDAlO1xufSJdfQ== */"

/***/ }),

/***/ "./src/app/exercise-table/exercise-table.component.html":
/*!**************************************************************!*\
  !*** ./src/app/exercise-table/exercise-table.component.html ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<table mat-table [dataSource]=\"dataSource\" class=\"mat-elevation-z8\">\n  \n    <!-- Date -->\n    <ng-container matColumnDef=\"date\">\n      <th mat-header-cell *matHeaderCellDef> Date </th>\n      <td mat-cell *matCellDef=\"let element\"> {{element.date}} </td>\n    </ng-container>\n  \n    <!-- Time of Exercise -->\n    <ng-container matColumnDef=\"time\">\n      <th mat-header-cell *matHeaderCellDef> Exercise Time </th>\n      <td mat-cell *matCellDef=\"let element\"> {{element.time}} </td>\n    </ng-container>\n  \n    <!-- Mean Score -->\n    <ng-container matColumnDef=\"score\">\n      <th mat-header-cell *matHeaderCellDef> Score [%] </th>\n      <td mat-cell *matCellDef=\"let element\"> {{element.score}} </td>\n    </ng-container>\n  \n    <tr mat-header-row *matHeaderRowDef=\"displayedColumns\"></tr>\n    <tr mat-row *matRowDef=\"let row; columns: displayedColumns;\"></tr>\n  </table>\n  "

/***/ }),

/***/ "./src/app/exercise-table/exercise-table.component.ts":
/*!************************************************************!*\
  !*** ./src/app/exercise-table/exercise-table.component.ts ***!
  \************************************************************/
/*! exports provided: ExerciseTableComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ExerciseTableComponent", function() { return ExerciseTableComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var ELEMENT_DATA = [
    { time: '2pm', date: '02.02.2019', score: 86 },
    { time: '6pm', date: '12.03.2019', score: 74 },
    { time: '10am', date: '28.03.2019', score: 69 },
    { time: '2pm', date: '11.04.2019', score: 91 }
];
var ExerciseTableComponent = /** @class */ (function () {
    function ExerciseTableComponent() {
        this.displayedColumns = ['date', 'time', 'score'];
        this.dataSource = ELEMENT_DATA;
    }
    ExerciseTableComponent.prototype.ngOnInit = function () {
    };
    ExerciseTableComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-exercise-table',
            template: __webpack_require__(/*! ./exercise-table.component.html */ "./src/app/exercise-table/exercise-table.component.html"),
            styles: [__webpack_require__(/*! ./exercise-table.component.css */ "./src/app/exercise-table/exercise-table.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], ExerciseTableComponent);
    return ExerciseTableComponent;
}());



/***/ }),

/***/ "./src/app/exercise/exercise.component.css":
/*!*************************************************!*\
  !*** ./src/app/exercise/exercise.component.css ***!
  \*************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".row {\n    display: flex;\n}\n\n.exercise-video-card {\n    max-width: 500px;\n    margin: 2px;\n}\n\n.exercise-record-card {\n    margin: 2px;\n}\n\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvZXhlcmNpc2UvZXhlcmNpc2UuY29tcG9uZW50LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtJQUNJLGNBQWM7Q0FDakI7O0FBRUQ7SUFDSSxpQkFBaUI7SUFDakIsWUFBWTtDQUNmOztBQUVEO0lBQ0ksWUFBWTtDQUNmIiwiZmlsZSI6InNyYy9hcHAvZXhlcmNpc2UvZXhlcmNpc2UuY29tcG9uZW50LmNzcyIsInNvdXJjZXNDb250ZW50IjpbIi5yb3cge1xuICAgIGRpc3BsYXk6IGZsZXg7XG59XG5cbi5leGVyY2lzZS12aWRlby1jYXJkIHtcbiAgICBtYXgtd2lkdGg6IDUwMHB4O1xuICAgIG1hcmdpbjogMnB4O1xufVxuXG4uZXhlcmNpc2UtcmVjb3JkLWNhcmQge1xuICAgIG1hcmdpbjogMnB4O1xufVxuIl19 */"

/***/ }),

/***/ "./src/app/exercise/exercise.component.html":
/*!**************************************************!*\
  !*** ./src/app/exercise/exercise.component.html ***!
  \**************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"row\">\n  <mat-card class=\"exercise-video-card\">\n    <mat-card-header>\n      <mat-card-title>Exercise 1</mat-card-title>\n    </mat-card-header>\n    <video src=\"\"></video>\n    <mat-card-actions>\n        <button mat-button>Start</button>\n        <button mat-button>Pause</button>\n      </mat-card-actions>\n    <mat-card-content>\n      <p>\n        Description of the exercise...\n      </p>\n    </mat-card-content>\n  </mat-card>\n\n  <mat-card class=\"exercise-record-card\">\n    <mat-card-header>\n      <mat-card-title>You</mat-card-title>\n    </mat-card-header>\n    <app-capture-camera></app-capture-camera>\n  </mat-card>\n</div>\n<div>\n    <app-exercise-table></app-exercise-table>\n</div>"

/***/ }),

/***/ "./src/app/exercise/exercise.component.ts":
/*!************************************************!*\
  !*** ./src/app/exercise/exercise.component.ts ***!
  \************************************************/
/*! exports provided: ExerciseComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ExerciseComponent", function() { return ExerciseComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _services_backend_service_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../services/backend-service.service */ "./src/app/services/backend-service.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var ExerciseComponent = /** @class */ (function () {
    function ExerciseComponent(route, backendService) {
        this.route = route;
        this.backendService = backendService;
        route.params.subscribe(function (param) {
            if (param.id) {
                backendService.getOnePose(0)
                    .subscribe(function (pose) { return console.log(pose); });
            }
        });
    }
    ExerciseComponent.prototype.ngOnInit = function () {
    };
    ExerciseComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-exercise',
            template: __webpack_require__(/*! ./exercise.component.html */ "./src/app/exercise/exercise.component.html"),
            styles: [__webpack_require__(/*! ./exercise.component.css */ "./src/app/exercise/exercise.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_2__["ActivatedRoute"],
            _services_backend_service_service__WEBPACK_IMPORTED_MODULE_1__["BackendServiceService"]])
    ], ExerciseComponent);
    return ExerciseComponent;
}());



/***/ }),

/***/ "./src/app/patient/patient.component.css":
/*!***********************************************!*\
  !*** ./src/app/patient/patient.component.css ***!
  \***********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".exercise-card {\n    max-width: 400px;\n}\n\n.mg-6 {\n    margin: 6px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvcGF0aWVudC9wYXRpZW50LmNvbXBvbmVudC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7SUFDSSxpQkFBaUI7Q0FDcEI7O0FBRUQ7SUFDSSxZQUFZO0NBQ2YiLCJmaWxlIjoic3JjL2FwcC9wYXRpZW50L3BhdGllbnQuY29tcG9uZW50LmNzcyIsInNvdXJjZXNDb250ZW50IjpbIi5leGVyY2lzZS1jYXJkIHtcbiAgICBtYXgtd2lkdGg6IDQwMHB4O1xufVxuXG4ubWctNiB7XG4gICAgbWFyZ2luOiA2cHg7XG59Il19 */"

/***/ }),

/***/ "./src/app/patient/patient.component.html":
/*!************************************************!*\
  !*** ./src/app/patient/patient.component.html ***!
  \************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<button class=\"mg-6\" mat-raised-button color=\"primary\" (click)=\"goToElectrodes()\">Attach Electrodes</button>\n<div>\n  <mat-card *ngFor=\"let p of pose\" class=\"exercise-card\">\n    <mat-card-header>\n      <mat-card-title>\n        {{p}}\n      </mat-card-title>\n    </mat-card-header>\n    <img mat-card-image src=\"https://material.angular.io/assets/img/examples/shiba2.jpg\" alt=\"Teaser of exercise 1\">\n    <mat-card-content>\n      <p>\n        Lorem ipsum dolor sit amet consectetur adipisicing elit.\n      </p>\n    </mat-card-content>\n    <mat-card-actions>\n      <button mat-raised-button color=\"primary\" (click)=\"goToExercise(1)\">Exercise</button>\n    </mat-card-actions>\n  </mat-card>\n</div>"

/***/ }),

/***/ "./src/app/patient/patient.component.ts":
/*!**********************************************!*\
  !*** ./src/app/patient/patient.component.ts ***!
  \**********************************************/
/*! exports provided: PatientComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "PatientComponent", function() { return PatientComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _services_backend_service_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../services/backend-service.service */ "./src/app/services/backend-service.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var PatientComponent = /** @class */ (function () {
    function PatientComponent(backendService, router) {
        var _this = this;
        this.backendService = backendService;
        this.router = router;
        this.pose = [];
        this.serviceSubscription = backendService.getPoses()
            .subscribe(function (pose) {
            _this.pose.push(pose);
        });
    }
    PatientComponent.prototype.ngOnInit = function () {
    };
    PatientComponent.prototype.goToExercise = function (id) {
        this.router.navigate(['exercise/' + id]);
    };
    PatientComponent.prototype.goToElectrodes = function () {
        this.router.navigate(['electrodes']);
    };
    PatientComponent.prototype.ngOnDestroy = function () {
        if (this.serviceSubscription) {
            this.serviceSubscription.unsubscribe();
        }
    };
    PatientComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-patient',
            template: __webpack_require__(/*! ./patient.component.html */ "./src/app/patient/patient.component.html"),
            styles: [__webpack_require__(/*! ./patient.component.css */ "./src/app/patient/patient.component.css")]
        }),
        __metadata("design:paramtypes", [_services_backend_service_service__WEBPACK_IMPORTED_MODULE_1__["BackendServiceService"],
            _angular_router__WEBPACK_IMPORTED_MODULE_2__["Router"]])
    ], PatientComponent);
    return PatientComponent;
}());



/***/ }),

/***/ "./src/app/services/backend-service.service.ts":
/*!*****************************************************!*\
  !*** ./src/app/services/backend-service.service.ts ***!
  \*****************************************************/
/*! exports provided: BackendServiceService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "BackendServiceService", function() { return BackendServiceService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var httpOptions = {
    headers: new _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpHeaders"]({
        'Content-Type': 'application/json'
    })
};
var BackendServiceService = /** @class */ (function () {
    function BackendServiceService(http) {
        this.http = http;
        this.BASE_URL = 'https://physio.test.sqooba.io/api/';
    }
    BackendServiceService.prototype.getPoses = function () {
        return this.http.get(this.BASE_URL + 'poses', httpOptions);
    };
    BackendServiceService.prototype.getOnePose = function (id) {
        return this.http.get(this.BASE_URL + 'poses/' + id.toString(), httpOptions);
    };
    BackendServiceService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"]])
    ], BackendServiceService);
    return BackendServiceService;
}());



/***/ }),

/***/ "./src/environments/environment.ts":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
var environment = {
    production: false
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "./src/main.ts":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser-dynamic */ "./node_modules/@angular/platform-browser-dynamic/fesm5/platform-browser-dynamic.js");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "./src/app/app.module.ts");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./environments/environment */ "./src/environments/environment.ts");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_3__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
}
Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(function (err) { return console.error(err); });


/***/ }),

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! /Users/florent/code/arkathon/physio-posenet/frontend/arkathon-frontend/src/main.ts */"./src/main.ts");


/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map