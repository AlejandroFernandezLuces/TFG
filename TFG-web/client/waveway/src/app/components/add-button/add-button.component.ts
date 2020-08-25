import { Component, OnInit, ViewChild, ElementRef  } from '@angular/core';
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
  fileToUpload: File = null;
  returnedValues: any;
  uploadFile(files: FileList) {
    
      this.fileToUpload = files.item(0);
      this.returnedValues = this._towdataService.upload(1, this.fileToUpload)
      console.log("this.returnedValues")
  }
  deleteAttachment(index) {
    this.fileToUpload.slice(index, 1);
  }
}
