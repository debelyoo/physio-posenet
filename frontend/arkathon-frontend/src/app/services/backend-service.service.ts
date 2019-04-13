import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class BackendServiceService {

  private BASE_URL = 'https://physio.test.sqooba.io/api/';

  constructor(private http: HttpClient) { }

  getPoses (): Observable<any> {
    return this.http.get(
      this.BASE_URL + 'poses', httpOptions);
  }

  getOnePose (id: number): Observable<any> {
    return this.http.get(
      this.BASE_URL + 'poses/' + id.toString(), httpOptions);
  }
}
