import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PosesComponent } from './poses/poses.component';
import { AppComponent } from './app.component';
import { CaptureCameraComponent } from './capture-camera/capture-camera.component';

const routes: Routes = [
  // { path: '', component: DashBoardComponent },
  { path: 'poses', component: PosesComponent },
  { path: 'record', component: CaptureCameraComponent },
  // { path: 'poses/:id',      component: PosesDetailComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
