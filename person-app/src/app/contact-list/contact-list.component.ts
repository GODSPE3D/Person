import { Component, Input, OnInit } from '@angular/core';
import { Contact } from '../person';
import { PersonService } from '../person.service';

@Component({
  selector: 'app-contact-list',
  templateUrl: './contact-list.component.html',
  styleUrls: ['./contact-list.component.css']
})
export class ContactListComponent implements OnInit {
  @Input() contactList: Contact[] = [];
  @Input() addContact: Contact[] = [];

  contactL: Contact[] = [];

  displayInput: boolean = false;

  constructor(private personService: PersonService) {}

  ngOnInit() {
    // this.personService.getAllContact().subscribe(con => {
    //   this.contactL = con;
    // });
  }
}
