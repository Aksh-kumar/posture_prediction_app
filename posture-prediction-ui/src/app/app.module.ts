import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { PosturePredictionComponent } from './posture-prediction/posture-prediction.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { DialogBoxComponent } from './dialog-box/dialog-box.component';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { MatDialogModule } from '@angular/material/dialog';
import { MatTableModule } from '@angular/material/table';

@NgModule({
  declarations: [
    AppComponent,
    PosturePredictionComponent,
    DialogBoxComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    MatTableModule,
    MatDialogModule,
    HttpClientModule,
    NoopAnimationsModule
  ],
  providers: [],
  entryComponents: [DialogBoxComponent],
  bootstrap: [AppComponent]
})
export class AppModule { }
