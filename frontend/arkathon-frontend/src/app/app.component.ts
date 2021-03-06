import { Component } from '@angular/core';
import { Router } from '@angular/router';
import {Location} from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor (private router: Router,
    private _location: Location) {
  }

  public openPatientPage () {
    this.router.navigate(['patient']);
  }

  public openDoctorPage () {
    this.router.navigate(['doctor']);
  }

  public seeCharts () {
    this.router.navigate(['charts']);
  }

  public goBack () {
    this._location.back();
  }

  public goHome () {
    this.router.navigate(['']);
  }
}
