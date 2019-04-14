import { Component, OnInit, OnDestroy, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
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
  private URL = 'https://physio.test.sqooba.io/api';
  private readonly routeSubscription: Subscription;
  private backendSubscription: Subscription;

  @ViewChild('videoElement') videoElement: any;
  private video: any;
  public videoOn = false;
  public interval;

  public picture;

  @ViewChild("canvas")
  public canvas: ElementRef;

  constructor (private route: ActivatedRoute,
    private backendService: BackendServiceService,
    private http: HttpClient) {
   }

  ngOnInit () {
    this.video = this.videoElement.nativeElement;
    this.backendSubscription = this.backendService.getPoses()
      .subscribe((pose) => {
      this.picture = this.URL + pose[0].thumbnail
    });
  }

  public takePicture() {
    this.initCamera({ video: true, audio: false });
    this.interval = setInterval(() => {
      let ctx = this.canvas.nativeElement.getContext('2d');
      ctx.drawImage(this.video, 0, 0, this.canvas.nativeElement.width, this.canvas.nativeElement.height);
      let img = new Image();
      img.src = this.canvas.nativeElement.toDataURL("image/png");
      this.http.post(this.URL + 1337 + "/check", img).subscribe(() => console.log(1));
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
