import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CaptureCameraComponent } from './capture-camera/capture-camera.component';
import { PatientComponent } from './patient/patient.component';
import { ExerciseComponent } from './exercise/exercise.component';
import { ElectrodesComponent } from './electrodes/electrodes.component';
import { DoctorViewComponent } from './doctor-view/doctor-view.component';

const routes: Routes = [
  { path: 'patient', component: PatientComponent },
  { path: 'exercise/:id', component: ExerciseComponent },
  { path: 'record', component: CaptureCameraComponent },
  { path: 'electrodes', component: ElectrodesComponent },
  { path: 'doctor', component: DoctorViewComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
