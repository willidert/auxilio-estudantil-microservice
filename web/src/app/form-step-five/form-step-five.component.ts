import { Component, OnInit } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-five',
  templateUrl: './form-step-five.component.html',
  styleUrls: ['./form-step-five.component.scss'],
})
export class FormStepFiveComponent implements OnInit {
  formQuestions: UserFormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }
  ngOnInit(): void {}

  log() {
    console.log('12 -', this.formQuestions.questionTwelve);
    console.log('13 -', this.formQuestions.questionThirteen);
  }
}
