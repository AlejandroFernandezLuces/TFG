import { Injectable } from '@angular/core';
import { HttpClient, HttpEvent, HttpErrorResponse, HttpEventType } from  '@angular/common/http';  
import { HttpHeaders } from '@angular/common/http';
import { GraphDrawService } from 'src/app/services/graphDraw/graph-draw.service'

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    'response-Type': 'json'
     })
};
@Injectable({
  providedIn: 'root'
})
export class TowdataService {
  fileContent: ArrayBuffer;
  constructor(private httpClient: HttpClient) { }
  
   public async upload(id: number, fileToUpload: File){
      const endpoint = 'http://localhost:8080/towdata';
      const formData: FormData = new FormData();
      var dataArray: any;
      const stringContent = await (await fileToUpload.text()).toString();
      var jsonBuild = 
      {   
        "id": 1,
        "csv": stringContent 
      };
      formData.append('fileKey', fileToUpload, fileToUpload.name);
      console.log(jsonBuild);

      
      return this.httpClient
        .post(endpoint, jsonBuild, httpOptions).subscribe(
          (val) => {
              console.log("POST call successful value returned in body")
              let drawGraph = new GraphDrawService()
              drawGraph.draw(val)
          },
          response => {
              console.log("POST call in error", response);
          },
          () => {
              console.log("The POST observable is now completed.");
          });
 
  }
}

