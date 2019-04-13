import { Component, OnInit } from '@angular/core';
import { BackendServiceService } from '../services/backend-service.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-exercise',
  templateUrl: './exercise.component.html',
  styleUrls: ['./exercise.component.css']
})
export class ExerciseComponent implements OnInit {

  constructor (private route: ActivatedRoute,
    private backendService: BackendServiceService) {
      route.params.subscribe((param) => {
        if (param.id) {
          backendService.getOnePose(0)
          .subscribe(
            (pose) => console.log(pose)
          );
        }
      });
   }

  ngOnInit () {
  }

}
