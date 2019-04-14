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
  private poseId;

  @ViewChild('canvas')
  public canvas: ElementRef;

  constructor (private route: ActivatedRoute,
    private backendService: BackendServiceService,
    private http: HttpClient) {
   }

  ngOnInit () {
    this.video = this.videoElement.nativeElement;
    this.backendSubscription = this.backendService.getPoses()
      .subscribe((pose) => {
      this.picture = this.URL + pose[0].thumbnail;
      this.poseId = pose[0].poseid;
    });
  }

  public takePicture() {
    this.initCamera({ video: true, audio: false });
    this.interval = setInterval(() => {
      const ctx = this.canvas.nativeElement.getContext('2d');
      ctx.drawImage(this.video, 0, 0, this.canvas.nativeElement.width, this.canvas.nativeElement.height);
      const img = new Image();
      img.src = this.canvas.nativeElement.toDataURL('image/png');
      let blobBin = atob(img.src.split(',')[1]);
      let ia = new Uint8Array(blobBin.length);
      for (let i = 0; i < blobBin.length; i++) {
          ia[i] = blobBin.charCodeAt(i);
      }
      let file = new Blob([ia], {type: 'image/png'});
      const formData = new FormData();
      formData.append('file', file);
      this.http.post(this.URL + "/poses/" + this.poseId + '/check', formData)
      .subscribe((response) => console.log(response));
    }, 2000);
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

  public getStyle() {
    return {
      'color': '#fff',
      'height': '10px',
      'width': '10px'
    };
  }

  private setStyle (response) {

  }

}
