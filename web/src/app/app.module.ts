import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { FormStepOneComponent } from './form-step-one/form-step-one.component';
import { FormStepTwoComponent } from './form-step-two/form-step-two.component';
import { FormStepThreeComponent } from './form-step-three/form-step-three.component';
import { FormStepFourComponent } from './form-step-four/form-step-four.component';
import { FormStepFiveComponent } from './form-step-five/form-step-five.component';
import { FormStepSixComponent } from './form-step-six/form-step-six.component';
import { UserEmailComponent } from './user-email/user-email.component';
import { FormStepSevenComponent } from './form-step-seven/form-step-seven.component';

@NgModule({
  declarations: [
    AppComponent,
    FormStepOneComponent,
    FormStepTwoComponent,
    FormStepThreeComponent,
    FormStepFourComponent,
    FormStepFiveComponent,
    FormStepSixComponent,
    UserEmailComponent,
    FormStepSevenComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
