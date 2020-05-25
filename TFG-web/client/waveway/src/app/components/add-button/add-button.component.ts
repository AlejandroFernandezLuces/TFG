import { Component, OnInit, ViewChild, ElementRef  } from '@angular/core';
import { HttpEventType, HttpErrorResponse } from '@angular/common/http';
import { of } from 'rxjs';  
import { catchError, map } from 'rxjs/operators';  
import { TowdataService} from  'src/app/services/towdata.service';

@Component({
  selector: 'app-add-button',
  templateUrl: './add-button.component.html',
  styleUrls: ['./add-button.component.css']
})
export class AddButtonComponent implements OnInit {

  constructor(private _towdataService: TowdataService) { }

  ngOnInit(): void {

  }
  files: any = [];

  uploadFile(file: File) {
      this._towdataService.upload(1, file)

  }
  deleteAttachment(index) {
    this.files.splice(index, 1)
  }
}
