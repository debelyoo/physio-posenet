import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-capture-camera',
  templateUrl: './capture-camera.component.html',
  styleUrls: ['./capture-camera.component.css']
})
export class CaptureCameraComponent implements OnInit {
    constructor() {
    }
    @ViewChild('videoElement') videoElement: any;  
    video: any;
  
    ngOnInit() {
      this.video = this.videoElement.nativeElement;
    }

    start() {
      this.initCamera({ video: true, audio: false });
    }

    stop(){
      this.video.pause();
    }
    
    initCamera(config:any) {
      var browser = <any>navigator;
  
      browser.getUserMedia = (browser.getUserMedia ||
        browser.webkitGetUserMedia ||
        browser.mozGetUserMedia ||
        browser.msGetUserMedia);
  
      browser.mediaDevices.getUserMedia(config).then(stream => {
        this.video.srcObject=stream;
        this.video.play();
      });
    }

}
