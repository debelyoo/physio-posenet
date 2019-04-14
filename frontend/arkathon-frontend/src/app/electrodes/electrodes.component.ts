import { Component, OnInit, ViewChild, ElementRef, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { BackendServiceService } from '../services/backend-service.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-electrodes',
  templateUrl: './electrodes.component.html',
  styleUrls: ['./electrodes.component.css']
})
export class ElectrodesComponent implements OnInit, OnDestroy {

  private URL = 'https://physio.test.sqooba.io/api/PICTURE_ENDPOINT/';
  private readonly routeSubscription: Subscription;
  private backendSubscription: Subscription;

  @ViewChild('videoElement2') videoElement2: any;
  private video2: any;
  public videoOn = false;
  public interval;

  @ViewChild('canvas2')
  public canvas2: ElementRef;

  public picture;

  constructor (private route: ActivatedRoute,
    private backendService: BackendServiceService,
    private http: HttpClient) {
   }

  ngOnInit () {
    this.video2 = this.videoElement2.nativeElement;
  }

  public record() {
    this.initCamera({ video: true, audio: false });
    this.interval = setInterval(() => {
      const ctx = this.canvas2.nativeElement.getContext('2d');
      ctx.drawImage(this.video2, 0, 0, this.canvas2.nativeElement.width, this.canvas2.nativeElement.height);
      const img = new Image();
      img.src = this.canvas2.nativeElement.toDataURL('image/png');
      /* this.http.post(this.URL + 1337 + "/check", img).subscribe(() => console.log(1)); */
    }, 1000);
  }

  private initCamera (config: any) {
    const browser = <any>navigator;

    browser.getUserMedia = (browser.getUserMedia ||
      browser.webkitGetUserMedia ||
      browser.mozGetUserMedia ||
      browser.msGetUserMedia);

    browser.mediaDevices.getUserMedia(config)
    .then((stream) => {
      this.video2.srcObject = stream;
      this.video2.play();
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
