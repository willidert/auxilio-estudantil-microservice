import { Component, OnInit } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-form-step-six',
  templateUrl: './form-step-six.component.html',
  styleUrls: ['./form-step-six.component.scss'],
})
export class FormStepSixComponent implements OnInit {
  formQuestions: UserFormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }

  ngOnInit(): void {}

  log() {
    console.log('14. -', this.formQuestions.questionFourteen);
    console.log('15. -', this.formQuestions.questionFifteen);
    console.log('16. -', this.formQuestions.questionSixteen);
    console.log('17. -', this.formQuestions.questionSeventeen);
    console.log('18. -', this.formQuestions.questionEighteen);
  }
}
