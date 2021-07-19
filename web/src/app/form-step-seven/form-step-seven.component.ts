import { Component, OnInit } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-seven',
  templateUrl: './form-step-seven.component.html',
  styleUrls: ['./form-step-seven.component.scss'],
})
export class FormStepSevenComponent implements OnInit {
  formQuestions: UserFormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }

  ngOnInit(): void {}

  log() {
    console.log('20. -', this.formQuestions.questionTwenty);
    console.log('21. -', this.formQuestions.questionTwentyOne);
    console.log('22. -', this.formQuestions.questionTwentyTwo);
  }

  submitForm() {
    console.log('Form been submitted');

    this.formDataService.sendFormQuestions();
  }
}
