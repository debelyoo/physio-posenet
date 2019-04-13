import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ChartsModule } from 'ng2-charts';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {MatButtonModule, MatCheckboxModule} from '@angular/material';
import {MatCardModule} from '@angular/material/card';
import { CaptureCameraComponent } from './capture-camera/capture-camera.component';
import { PatientComponent } from './patient/patient.component';
import { BackendServiceService } from './services/backend-service.service';
import { HttpClientModule } from '@angular/common/http';
import { ExerciseComponent } from './exercise/exercise.component';
import {MatProgressBarModule} from '@angular/material/progress-bar';
import { ExerciseTableComponent } from './exercise-table/exercise-table.component';
import {MatTableModule} from '@angular/material/table';
import { ElectrodesComponent } from './electrodes/electrodes.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import { DoctorViewComponent } from './doctor-view/doctor-view.component';
import { GamificationComponent } from './gamification/gamification.component';
import { VideoExerciseComponent } from './video-exercise/video-exercise.component';

@NgModule({
  declarations: [
    AppComponent,
    PatientComponent,
    CaptureCameraComponent,
    ExerciseComponent,
    ExerciseTableComponent,
    ElectrodesComponent,
    DoctorViewComponent,
    GamificationComponent,
    VideoExerciseComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    MatButtonModule,
    MatCheckboxModule,
    MatCardModule,
    MatProgressBarModule,
    MatTableModule,
    MatToolbarModule,
    ChartsModule
  ],
  providers: [BackendServiceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
