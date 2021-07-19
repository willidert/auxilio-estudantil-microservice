import { Component, OnInit } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-three',
  templateUrl: './form-step-three.component.html',
  styleUrls: ['./form-step-three.component.scss'],
})
export class FormStepThreeComponent implements OnInit {
  formQuestions: UserFormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }

  ngOnInit(): void {}

  log() {
    console.log('7. -', this.formQuestions.questionSeven);
    console.log('8. -', this.formQuestions.questionEight);
    console.log('9. -', this.formQuestions.questionNine);
  }
}
