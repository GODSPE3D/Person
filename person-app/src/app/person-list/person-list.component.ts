import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';

import { Person } from '../person';
import { PersonService } from '../person.service';
import { PersonDetailComponent } from '../person-detail/person-detail.component';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrls: ['./person-list.component.css'],
  providers: []
})
export class PersonListComponent implements OnInit {

  searchText!: string;
  person: Person[] = [];

  @ViewChild(PersonDetailComponent) child!: PersonDetailComponent;

  constructor(private personService: PersonService, public dialog: MatDialog) { }

  ngOnInit() {
    this.getPersonAll();
  }

  getPersonAll() {
    this.personService.getAll()
      .subscribe(person => {
        console.log(person);
        this.person = person
      });
      // console.log(this.person);
  }

  addPerson(addP: Person) {
    this.personService.addPerson(addP).subscribe(addP => {
      this.getPersonAll();
    });
    this.person.push(addP);
    // this.personService.addPerson(outP).subscribe();
    // this.person.push(this.child.newP);
  }

  delete(p: Person): void {
    this.person = this.person.filter(h => h !== p);
    this.personService.deletePerson(p._id).subscribe(son => {
      this.getPersonAll();
    });
  }
}