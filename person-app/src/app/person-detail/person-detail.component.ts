import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Person } from '../person';
import { PersonService } from '../person.service';

@Component({
  selector: 'app-person-detail',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.css']
})
export class PersonDetailComponent {
  @Input() newP!: Person;
  // newP: Person | undefined;

  constructor(private personService: PersonService, private location: Location) {}

  ngOnInit(): void {
  }

  // getP(): void {
  //   const id = parseInt(this.route.snapshot.paramMap.get('id')!, 10);
  //   this.personService.getP(id).subscribe()
  // }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    if (this.newP) {
      this.personService.updatePerson(this.newP).subscribe(() => this.goBack())
    }
  }

}
