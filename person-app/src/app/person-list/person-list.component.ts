import { Component, DEFAULT_CURRENCY_CODE, OnInit, PipeTransform, ViewChild } from '@angular/core';

import { MatDialog } from '@angular/material/dialog';
import { Person } from '../person';
import { PersonDetailComponent } from '../person-detail/person-detail.component';
import { PersonService } from '../person.service';
import { FormControl } from '@angular/forms';
// import { DecimalPipe } from '@angular/common';
// import { Observable, map, startWith } from 'rxjs';
import { Button } from 'bootstrap';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrls: ['./person-list.component.css'],
  providers: []
})
export class PersonListComponent implements OnInit {

  button = Button;
  page = 1;
  pageSize = 10;
  collectionSize: number = 0;
  searchText = '';
  person: Person[] = [];
  filterPerson: Person[] = [];
  pagePerson: Person[] = [];
  // p = {} as Person;
  filter = new FormControl('', { nonNullable: true });

  public newP = <Person>{};

  @ViewChild(PersonDetailComponent) child!: PersonDetailComponent;

  constructor(public personService: PersonService, public dialog: MatDialog) {
    this.refreshCountries();
  }

  // buttonSearch(pipe: DecimalPipe) {
  //   this.person = this.filter.valueChanges.pipe(
  // 		startWith(''),
  // 		map((text) => this.search(text, pipe)),
  // 	);
  // }

  ngOnInit() {
    this.getPersonAll();
    // this.getOne();
    // this.postM();
  }

  toggle() {
    this.button.getOrCreateInstance;
    // this.button.jQueryInterface("toggle");
  }

  getPersonAll() {
    this.personService.getAll()
      .subscribe(person => {
        // console.log(person);
        this.person = person
        // this.collectionSize = this.person.length;
        this.filterPerson = this.person;
      });
    // this.refreshCountries();
    // console.log(this.person);
  }

  refreshCountries() {
		this.pagePerson = this.filterPerson.map((country, i) => ({ x: i + 1, ...country })).slice(
			(this.page - 1) * this.pageSize,
			(this.page - 1) * this.pageSize + this.pageSize,
		);
	}

  // filterResults(text: string) {
  //   return this.filterPerson.filter((country) => {
  //     // if (!text) {
  //     //   this.filterPerson = this.person;
  //     // }

  //     const term = text.toLowerCase();
  //     return (
  //       country.firstname.toLowerCase().includes(term) ||
  //       country.lastname.toLowerCase().includes(term) ||
  //       country.email.toLowerCase().includes(term)
  //     );
  //   });
  // }

  filterResults(text: string) {
    if (!text) {
      this.filterPerson = this.person;
    }

    this.filterPerson = this.person.filter(
      person => person.firstname.toLowerCase().includes(text.toLowerCase()) || person.lastname.toLowerCase().includes(text.toLowerCase()) || person.email.toLowerCase().includes(text.toLowerCase())
    );
  }

  getOne() {
    this.personService.getPerson(5).subscribe(newP => {
      this.newP = newP;
    })
  }

  // postM() {
  //   this.personService.postMail().subscribe(newV => {
  //     this.newP = newV;
  //     // console.log("newP -> ", this.newP);
  //   })
  // }

  addPerson(addP: Person) {
    this.personService.addPerson(addP).subscribe(addP => {
      // this.getPersonAll();
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