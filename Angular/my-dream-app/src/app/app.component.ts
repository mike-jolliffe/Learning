import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  name = '';
  displayText = false;
  log = [];

  onToggleDetails() {
    this.displayText = !this.displayText;
    this.log.push(new Date());
  }
}
