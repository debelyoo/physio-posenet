import { Component, OnInit, ViewChild } from '@angular/core';
import { timer } from 'rxjs/internal/observable/timer';
import { Subscription } from 'rxjs';

const source = timer(1, 1000);

@Component({
  selector: 'app-capture-camera',
  templateUrl: './capture-camera.component.html',
  styleUrls: ['./capture-camera.component.css']
})
export class CaptureCameraComponent implements OnInit {
  @ViewChild('videoElement') videoElement: any;
  private video: any;
  public videoOn = false;

  public color = 'primary';
  public mode = 'determinate';
  public value = 0;

  public tick = 0;
  timerSubscription: Subscription;

  private countable = false;
  public count = 0;

  constructor() {
  }

  ngOnInit() {
    this.video = this.videoElement.nativeElement;
  }

  public start () {
    this.countable = true;
    this.videoOn = true;
    this.initCamera({ video: true, audio: false });
    this.startTimer();
    this.value = 60;
    this.setRandomProgress();
  }

  public stop () {
    this.video.pause();
    this.pauseTimer();
    if (this.countable) {
      this.count++;
      this.countable = false;
    }
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

  private startTimer () {
    this.timerSubscription = source.subscribe(tick => this.tick = tick);
  }

  private pauseTimer () {
    if (this.timerSubscription) {
      this.timerSubscription.unsubscribe();
    }
  }

  private setRandomProgress () {
    setInterval(() => {
      this.value = Math.floor(Math.random() * 40) + 60;
    }, 1000);
  }

}
