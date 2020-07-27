import { Injectable } from '@angular/core';
import { HttpClient, HttpEvent, HttpErrorResponse, HttpEventType } from  '@angular/common/http';  
import { map } from  'rxjs/operators';
import { stringify } from 'querystring';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'text/plain',
     'Access-Control-Allow-Origin': 'localhost',
     'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
     'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token'
     })
};
@Injectable({
  providedIn: 'root'
})
export class TowdataService {
  fileContent: ArrayBuffer;
  constructor(private httpClient: HttpClient) { }
    
   public upload(id: number, fileToUpload: File){
      const endpoint = 'http://localhost:8080/towdata';
      const formData: FormData = new FormData();

      formData.append('fileKey', fileToUpload, fileToUpload.name);
      return this.httpClient
        .post(endpoint, formData, httpOptions).subscribe(
          (val) => {
              console.log("POST call successful value returned in body", 
                          val);
          },
          response => {
              console.log("POST call in error", response);
          },
          () => {
              console.log("The POST observable is now completed.");
          });
  }
}

