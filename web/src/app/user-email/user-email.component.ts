import { Component, OnInit } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';
import { FormDataService } from '../services/form-data.service';

@Component({
  selector: 'app-user-email',
  templateUrl: './user-email.component.html',
  styleUrls: ['./user-email.component.scss'],
})
export class UserEmailComponent implements OnInit {
  formQuestions: UserFormQuestions;

  constructor(public formDataService: FormDataService) {
    this.formQuestions = formDataService.formQuestions;
  }

  ngOnInit(): void {}
}
