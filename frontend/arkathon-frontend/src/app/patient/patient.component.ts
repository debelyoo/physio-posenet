import { Component, OnInit, OnDestroy } from '@angular/core';
import { BackendServiceService } from '../services/backend-service.service';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent implements OnInit, OnDestroy {

  private readonly serviceSubscription: Subscription;

  public pose = [];

  constructor (private backendService: BackendServiceService,
    private router: Router) {
    this.serviceSubscription = backendService.getPoses()
    .subscribe((pose) => {
      this.pose.push(pose);
    });
  }

  ngOnInit () {
  }

  public goToPictureExercise (id) {
    this.router.navigate(['exercise/' + id]);
  }

  public goToVideoExercise (id) {
    this.router.navigate(['vidExercise/' + id]);
  }

  public goToElectrodes () {
    this.router.navigate(['electrodes']);
  }

  ngOnDestroy () {
    if (this.serviceSubscription) {
      this.serviceSubscription.unsubscribe();
    }
  }

}
