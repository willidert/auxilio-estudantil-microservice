import { Component, OnInit } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-four',
  templateUrl: './form-step-four.component.html',
  styleUrls: ['./form-step-four.component.scss'],
})
export class FormStepFourComponent implements OnInit {
  formQuestions: UserFormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }
  ngOnInit(): void {}

  log() {
    console.log('10 -', this.formQuestions.questionTen);
    console.log('11 -', this.formQuestions.questionEleven);
  }
}
