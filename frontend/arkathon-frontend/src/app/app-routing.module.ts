import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CaptureCameraComponent } from './capture-camera/capture-camera.component';
import { PatientComponent } from './patient/patient.component';
import { ExerciseComponent } from './exercise/exercise.component';
import { ElectrodesComponent } from './electrodes/electrodes.component';
import { DoctorViewComponent } from './doctor-view/doctor-view.component';
import { GamificationComponent } from './gamification/gamification.component';
import { VideoExerciseComponent } from './video-exercise/video-exercise.component';
import { ExerciseTwoComponent } from './exercise-two/exercise-two.component';

const routes: Routes = [
  { path: 'patient', component: PatientComponent },
  { path: 'exercise/1', component: ExerciseComponent },
  { path: 'exercise/2', component: ExerciseTwoComponent },
  { path: 'vidExercise/:id', component: VideoExerciseComponent },
  { path: 'record', component: CaptureCameraComponent },
  { path: 'electrodes', component: ElectrodesComponent },
  { path: 'doctor', component: DoctorViewComponent },
  { path: 'charts', component: GamificationComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
