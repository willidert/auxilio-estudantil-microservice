import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FormStepFiveComponent } from './form-step-five/form-step-five.component';
import { FormStepFourComponent } from './form-step-four/form-step-four.component';
import { FormStepOneComponent } from './form-step-one/form-step-one.component';
import { FormStepSixComponent } from './form-step-six/form-step-six.component';
import { FormStepThreeComponent } from './form-step-three/form-step-three.component';
import { FormStepTwoComponent } from './form-step-two/form-step-two.component';

const routes: Routes = [
  { path: '', component: FormStepOneComponent },
  { path: 'form-step-two', component: FormStepTwoComponent },
  { path: 'form-step-three', component: FormStepThreeComponent },
  { path: 'form-step-four', component: FormStepFourComponent },
  { path: 'form-step-five', component: FormStepFiveComponent },
  { path: 'form-step-six', component: FormStepSixComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
