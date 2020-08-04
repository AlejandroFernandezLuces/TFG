import { Component, OnInit, ViewChild, ElementRef  } from '@angular/core';
import { HttpEventType, HttpErrorResponse } from '@angular/common/http';
import { of } from 'rxjs';  
import { catchError, map } from 'rxjs/operators';  
import { TowdataService} from  'src/app/services/towdata.service';
import { throwToolbarMixedModesError } from '@angular/material/toolbar';

@Component({
  selector: 'app-add-button',
  templateUrl: './add-button.component.html',
  styleUrls: ['./add-button.component.css']
})

export class AddButtonComponent implements OnInit {

  constructor(private _towdataService: TowdataService) { }

  ngOnInit(): void {

  }
  fileToUpload: File = null;

  uploadFile(files: FileList) {
    
      this.fileToUpload = files.item(0);
      this._towdataService.upload(1, this.fileToUpload)

  }
  deleteAttachment(index) {
    this.fileToUpload.slice(index, 1);
  }
}
