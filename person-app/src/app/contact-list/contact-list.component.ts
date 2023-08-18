import { Component, Input } from '@angular/core';
import { Contact } from '../person';

@Component({
  selector: 'app-contact-list',
  templateUrl: './contact-list.component.html',
  styleUrls: ['./contact-list.component.css']
})
export class ContactListComponent {
  @Input() contactList: Contact[] = [];
  @Input() addContact: Contact[] = [];

  displayInput: boolean = false;
}
