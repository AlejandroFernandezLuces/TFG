import { Injectable } from '@angular/core';
import { HttpClient, HttpEvent, HttpErrorResponse, HttpEventType } from  '@angular/common/http';  
import { map } from  'rxjs/operators';
import { stringify } from 'querystring';

@Injectable({
  providedIn: 'root'
})
export class TowdataService {
	endpoint: string = "http://localhost:8080/towdata";  

  constructor(private httpClient: HttpClient) { }
  public upload(id: number, file: File) {

    const formData: FormData = new FormData();

    formData.append('fileKey', file[0]);
    console.log(formData.get("fileKey"))
    console.log()
    return this.httpClient
    .post(this.endpoint, formData);
  }

}
