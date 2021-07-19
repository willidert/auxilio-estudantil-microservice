import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserFormQuestions } from '../models/user-form-questions';

@Injectable({
  providedIn: 'root',
})
export class FormDataService {
  formQuestions: UserFormQuestions;
  readonly apiURL: string;

  constructor(private http: HttpClient) {
    this.formQuestions = new UserFormQuestions();
    this.apiURL = 'http://localhost:3333';
  }

  sendFormQuestions() {
    this.http.post(`${this.apiURL}/`, this.formQuestions).subscribe(
      (val) => {
        console.log('POST call successful value returned in body', val);
      },
      (response) => {
        console.log('POST call in error', response);
      },
      () => {
        console.log('The POST observable is now completed.');
      }
    );
  }
}
