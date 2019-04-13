import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-doctor-view',
  templateUrl: './doctor-view.component.html',
  styleUrls: ['./doctor-view.component.css']
})
export class DoctorViewComponent implements OnInit, OnDestroy {

  private URL = 'https://physio.test.sqooba.io/api/poses';
  private fileToUpload;
  private postPoseSubscription: Subscription;

  constructor (public http: HttpClient) { }

  ngOnInit () {
  }

  public uploadPose(files: FileList) {
    this.fileToUpload = files.item(0);
    const formData = new FormData();
    formData.append('file', this.fileToUpload, this.fileToUpload.name);
    this.postPoseSubscription = this.http.post(this.URL, formData).subscribe((val) => {
      console.log(val);
    });
    return false;
  }

  ngOnDestroy () {
    if (this.postPoseSubscription) {
      this.postPoseSubscription.unsubscribe();
    }
  }
}
