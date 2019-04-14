import { Component, OnInit, ViewChild, ElementRef, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { BackendServiceService } from '../services/backend-service.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-exercise-two',
  templateUrl: './exercise-two.component.html',
  styleUrls: ['./exercise-two.component.css']
})
export class ExerciseTwoComponent implements OnInit, OnDestroy {
  private URL = 'https://physio.test.sqooba.io/api/poses/0/check';
  private readonly routeSubscription: Subscription;
  private backendSubscription: Subscription;

  @ViewChild('videoElement') videoElement: any;
  private video: any;
  public interval;

  @ViewChild('canvas') canvas: ElementRef;

  public picture = '';

  constructor (private route: ActivatedRoute,
    private backendService: BackendServiceService,
    private http: HttpClient) {
   }

  ngOnInit () {
    this.video = this.videoElement.nativeElement;
    /* this.backendSubscription = this.backendService.getPoses()
      .subscribe((pose) => {
      this.picture = this.URL + pose[0].thumbnail;
    }); */
  }

  public takePicture() {
    this.initCamera({ video: true, audio: false });
    this.interval = setInterval(() => {
      const ctx = this.canvas.nativeElement.getContext('2d');
      ctx.drawImage(this.video, 0, 0, this.canvas.nativeElement.width, this.canvas.nativeElement.height);
      const img = new Image();
      img.src = this.canvas.nativeElement.toDataURL('image/png');
      /* this.http.post(this.URL + 1337 + '/check', img).subscribe(() => console.log(1)); */
    },  1000);
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
