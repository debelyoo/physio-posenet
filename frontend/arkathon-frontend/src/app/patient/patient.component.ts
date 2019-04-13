import { Component, OnInit } from '@angular/core';
import { BackendServiceService } from '../services/backend-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent implements OnInit {

  public pose = [];

  constructor (private backendService: BackendServiceService,
    private router: Router) {
    backendService.getPoses()
    .subscribe((pose) => {
      this.pose.push(pose);
    });
  }

  ngOnInit () {
  }

  goToExercise (id) {
    this.router.navigate(['exercise/' + id]);
  }

}
