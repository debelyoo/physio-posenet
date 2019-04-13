import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { BackendServiceService } from '../services/backend-service.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-exercise-two',
  templateUrl: './exercise-two.component.html',
  styleUrls: ['./exercise-two.component.css']
})
export class ExerciseTwoComponent implements OnInit {
  private URL = 'https://physio.test.sqooba.io/api/poses/0/check';
  private readonly routeSubscription: Subscription;
  private backendSubscription: Subscription;

  @ViewChild('videoElement') videoElement: any;
  private video: any;
  public videoOn = false;
  public countDown: number = 7;
  public interval;
  public bigNumber = false;

  @ViewChild("canvas")
  public canvas: ElementRef;
  public captures: Array<any>;

  public picture = '';

  constructor (private route: ActivatedRoute,
    private backendService: BackendServiceService,
    private http: HttpClient) {
      this.routeSubscription = route.params.subscribe((param) => {
        if (param.id) {
          this. backendSubscription = backendService.getOnePose(0)
          .subscribe(
            (pose) => {
              this.picture = pose;
            }
          );
        }
      });
    this.captures = [];
   }

  ngOnInit () {
    this.video = this.videoElement.nativeElement;
  }

  public takePicture() {
    this.bigNumber = true;
    this.initCamera({ video: true, audio: false });
    this.interval = setInterval(() => {
      if(this.countDown > 0) {
        this.countDown--;
      } else {
        this.countDown = null;
        this.bigNumber = false; 
        this.captures.push(this.canvas.nativeElement.toDataURL("image/png"));
        this.http.post(this.URL, this.captures[0]);
        this.video.pause();
        setTimeout(() => clearInterval(this.interval), 500);
      };
    }, 1000)
  }

  public setFont () {
    return this.bigNumber ? 100 : 16;
  }

  private initCamera (config: any) {
    const browser = <any>navigator;

    browser.getUserMedia = (browser.getUserMedia ||
      browser.webkitGetUserMedia ||
      browser.mozGetUserMedia ||
      browser.msGetUserMedia);

    browser.mediaDevices.getUserMedia(config)
    .then((stream) => {
      this.video.srcObject = stream;
      this.video.play();
    });
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