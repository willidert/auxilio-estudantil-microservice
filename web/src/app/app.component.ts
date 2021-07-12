import { Component } from '@angular/core';
import { FormDataService } from './services/form-data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'web';

  constructor(public formDataService: FormDataService) {}
}
