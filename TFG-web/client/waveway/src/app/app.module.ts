import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BannerComponent } from './components/banner/banner.component';
import { AddButtonComponent } from './components/add-button/add-button.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { GraphComponent } from './components/graph/graph.component';


import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatIconModule} from '@angular/material/icon';
import {MatCardModule} from '@angular/material/card';
import {MatProgressBarModule} from '@angular/material/progress-bar';
import { DndDirective } from './components/add-button/dnd.directive';
import { TowdataService } from './services/towdata.service';
import { HttpClientModule } from "@angular/common/http";
import { UpdateButtonComponent } from './components/update-button/update-button.component';


@NgModule({
  declarations: [
    AppComponent,
    BannerComponent,
    AddButtonComponent,
    DndDirective,
    GraphComponent,
    UpdateButtonComponent
  ],
  imports: [
    BrowserModule,  
    BrowserAnimationsModule,  
    MatToolbarModule,  
    MatIconModule,  
    MatButtonModule,  
    MatCardModule,  
    MatProgressBarModule,
    HttpClientModule  
  ],
  exports: [
    MatButtonModule
  ],
  providers: [TowdataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
