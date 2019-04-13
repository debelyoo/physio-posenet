import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-doctor-view',
  templateUrl: './doctor-view.component.html',
  styleUrls: ['./doctor-view.component.css']
})
export class DoctorViewComponent implements OnInit {

  private URL = 'https://physio.test.sqooba.io/api/poses';
  private fileToUpload;

  constructor (public http: HttpClient) { }

  ngOnInit () {
  }

  public uploadPose(files: FileList) {
    this.fileToUpload = files.item(0);
    const formData = new FormData();
    formData.append('file', this.fileToUpload, this.fileToUpload.name);
    this.http.post(this.URL, formData).subscribe((val) => {
      console.log(val);
    });
    return false;
  }
}
