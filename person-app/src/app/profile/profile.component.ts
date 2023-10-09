import { Component, Input } from '@angular/core';
import { Person } from '../person';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  @Input() userData = {} as Person;
}
