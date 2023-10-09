import { Component, EventEmitter, Input, Output, TemplateRef, ViewChild } from '@angular/core';
import { Contact, Person } from '../person';
import { PersonService } from '../person.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent {
  // @Input() contactList: Contact[] = [];
  @Input() contact = {} as Contact;
  @Input() addContact = {} as Contact;
  // addContact: Contact[] = [];
  @ViewChild('addC') customDialog!: TemplateRef<any>;

  @Output() addC = new EventEmitter<Contact>();
  // @Output() addP = new EventEmitter<Person>();

  constructor(private personService: PersonService) {
  }

  ngOninit() {
    // console.log("contactList: ", this.contactList);
    console.log("contact ", this.contact);
  }

  // openDialog() {
  //   this.dialog.open(this.customDialog);
  // }
  addCont(addContact: Contact) {
    this.personService.addContact(addContact).subscribe(contact => {
      console.log(contact);
    })
  }
}
