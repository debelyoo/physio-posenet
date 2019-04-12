import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {MatButtonModule, MatCheckboxModule} from '@angular/material';
import { PosesComponent } from './poses/poses.component';
import { CaptureCameraComponent } from './capture-camera/capture-camera.component';

@NgModule({
  declarations: [
    AppComponent,
    PosesComponent,
    CaptureCameraComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatButtonModule,
    MatCheckboxModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
