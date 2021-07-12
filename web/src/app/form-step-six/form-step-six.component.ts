import { Component, OnInit } from '@angular/core';
import { FormQuestions } from '../models/form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-six',
  templateUrl: './form-step-six.component.html',
  styleUrls: ['./form-step-six.component.scss'],
})
export class FormStepSixComponent implements OnInit {
  formQuestions: FormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }

  ngOnInit(): void {}

  log() {
    console.log('14. -', this.formQuestions.questionsFourteen);
    console.log('15. -', this.formQuestions.questionsFifteen);
    console.log('16. -', this.formQuestions.questionsSixteen);
    console.log('17. -', this.formQuestions.questionsSeventeen);
    console.log('18. -', this.formQuestions.questionsEighteen);
  }

  submitForm() {
    console.log('Form been submitted');

    this.formDataService.sendFormQuestions();
  }
}
