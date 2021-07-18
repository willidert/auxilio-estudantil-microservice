import { Component, OnInit } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-two',
  templateUrl: './form-step-two.component.html',
  styleUrls: ['./form-step-two.component.scss'],
})
export class FormStepTwoComponent implements OnInit {
  formQuestions: UserFormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }
  ngOnInit(): void {}

  log() {
    console.log('4. -', this.formQuestions.questionFour);
    console.log('5. -', this.formQuestions.questionFive);
    console.log('6. -', this.formQuestions.questionSix);
  }
}
