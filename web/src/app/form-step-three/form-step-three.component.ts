import { Component, OnInit } from '@angular/core';
import { FormQuestions } from '../models/form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-three',
  templateUrl: './form-step-three.component.html',
  styleUrls: ['./form-step-three.component.scss'],
})
export class FormStepThreeComponent implements OnInit {
  formQuestions: FormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }

  ngOnInit(): void {}

  log() {
    console.log('7. -', this.formQuestions.questionSeven);
    console.log('8. -', this.formQuestions.questionsEight);
    console.log('9. -', this.formQuestions.questionsNine);
  }
}
