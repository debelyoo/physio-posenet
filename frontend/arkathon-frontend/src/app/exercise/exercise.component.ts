import { Component, OnInit, OnDestroy } from '@angular/core';
import { BackendServiceService } from '../services/backend-service.service';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-exercise',
  templateUrl: './exercise.component.html',
  styleUrls: ['./exercise.component.css']
})
export class ExerciseComponent implements OnInit, OnDestroy {

  private readonly routeSubscription: Subscription;
  private backendSubscription: Subscription;

  constructor (private route: ActivatedRoute,
    private backendService: BackendServiceService) {
      this.routeSubscription = route.params.subscribe((param) => {
        if (param.id) {
          this. backendSubscription = backendService.getOnePose(0)
          .subscribe(
            (pose) => console.log(pose)
          );
        }
      });
   }

  ngOnInit () {
  }

  ngOnDestroy () {
    if (this.routeSubscription) {
      this.routeSubscription.unsubscribe();
    }
    if (this.backendSubscription) {
      this.backendSubscription.unsubscribe();
    }
  }

}
