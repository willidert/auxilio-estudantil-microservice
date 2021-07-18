import { Component, OnInit } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-one',
  templateUrl: './form-step-one.component.html',
  styleUrls: ['./form-step-one.component.scss'],
})
export class FormStepOneComponent implements OnInit {
  formQuestions: UserFormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }

  ngOnInit(): void {}

  log() {
    console.log('1. -', this.formQuestions.questionOne);
    console.log('2. -', this.formQuestions.questionTwo);
    console.log('3. -', this.formQuestions.questionThree);
  }
}
