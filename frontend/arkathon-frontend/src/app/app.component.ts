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

  public goBack () {
    this._location.back();
  }
}
