import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';

import { Person } from '../person';
import { PersonService } from '../person.service';
import { PersonDetailComponent } from '../person-detail/person-detail.component';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute } from '@angular/router';
import { User } from '../user';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrls: ['./person-list.component.css'],
  providers: []
})
export class PersonListComponent implements OnInit {

  searchText!: string;
  person: Person[] = [];
  p!: Person;

  public newP = <Person>{};

  @ViewChild(PersonDetailComponent) child!: PersonDetailComponent;

  constructor(private personService: PersonService, public dialog: MatDialog) {}

  ngOnInit() {
    // this.getPersonAll();
    // this.getOne();
    this.postM();
  }

  getPersonAll() {
    this.personService.getAll()
      .subscribe(person => {
        console.log(person);
        this.person = person
      });
      // console.log(this.person);
  }

  getOne() {
    // this.personService.getPerson(5).subscribe((newValue: Person) => {
    //   // const x: User = {firstname: newValue.firstname, lastname: newValue.lastname, email: newValue.email};
    //   this.newP = newValue;
    //   console.log(this.newP);
    // }, error => {
    //   console.log(error);
    // }
    // );
    this.personService.getPerson(5).subscribe(newP => {
      this.newP = newP;
      console.log(this.newP);
    })
  }

  postM() {
    this.personService.postMail().subscribe(newV => {
      this.newP = newV;
      console.log("newP -> ", this.newP);
    })
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
    this.personService.deletePerson(p.id).subscribe(son => {
      this.getPersonAll();
    });
  }
}