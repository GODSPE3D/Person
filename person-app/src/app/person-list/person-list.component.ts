import { Component, Input, OnInit } from '@angular/core';

import { Person } from '../person';
import { PersonService } from '../person.service';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrls: ['./person-list.component.css']
})
export class PersonListComponent implements OnInit {

  public person: Person[] = [];
  // public p = this.person[0];

  constructor(private personService: PersonService) { }

  ngOnInit() {
    this.getPerson();
  }

  getPerson() {
    this.personService.getPerson().subscribe((data: Person[]) => {
      this.person = data;
      console.log(this.person);
    });
  }

  // getUserName(id: number) {
  //   this.personService.GetUser(id).pipe(map(response => {
  //     this.person = response;
  //   }))
  // }
}
