import { Component, OnInit, OnDestroy, ViewChild, ElementRef } from '@angular/core';
import { BackendServiceService } from '../services/backend-service.service';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-exercise',
  templateUrl: './exercise.component.html',
  styleUrls: ['./exercise.component.css']
})
export class ExerciseComponent implements OnInit, OnDestroy {
  private URL = 'https://physio.test.sqooba.io/api/poses/';
  private readonly routeSubscription: Subscription;
  private backendSubscription: Subscription;

  @ViewChild('videoElement') videoElement: any;
  private video: any;
  public videoOn = false;
  public interval;

  @ViewChild("canvas")
  public canvas: ElementRef;

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
   }

  ngOnInit () {
    this.video = this.videoElement.nativeElement;
  }

  public takePicture() {
    this.initCamera({ video: true, audio: false });
    this.interval = setInterval(() => {
      let ctx = this.canvas.nativeElement.getContext('2d');
      ctx.drawImage(this.video, 0, 0, this.canvas.nativeElement.width, this.canvas.nativeElement.height);
      let img = new Image();
      img.src = this.canvas.nativeElement.toDataURL("image/png");
      this.http.post(this.URL + 1337 + "/check", img).subscribe(res => console.log(res));
    }, 1000)
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
