import { Component, OnInit } from '@angular/core';
import { UpdateService} from  'src/app/services/updateService/update.service';

@Component({
  selector: 'app-update-button',
  templateUrl: './update-button.component.html',
  styleUrls: ['./update-button.component.css']
})
export class UpdateButtonComponent implements OnInit {

  constructor(private _updateService: UpdateService) { }

  ngOnInit(): void {

  }
  fileToUpload: File = null;
  returnedValues: any;
  updateFile(files: FileList) {
    
      this.fileToUpload = files.item(0);
      this.returnedValues = this._updateService.update(1, this.fileToUpload)
      console.log("this.returnedValues")
  }
  deleteAttachment(index) {
    this.fileToUpload.slice(index, 1);
  }

}
