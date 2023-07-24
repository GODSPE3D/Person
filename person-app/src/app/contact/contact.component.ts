import { Component, Input } from '@angular/core';
import { Contact } from '../person';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent {
  @Input() contactList: Contact[] = [];
  @Input() c = {} as Contact;

  ngOninit() {
    console.log("contactList: ", this.contactList);
    console.log("contact ", this.c);
  }
}
