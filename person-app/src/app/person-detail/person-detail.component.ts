import { Component, Input, Output, EventEmitter, DoCheck, ViewChild, Directive } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { JsonPipe, Location } from '@angular/common';

import { IPerson } from '../person';
import { PersonService } from '../person.service';

@Component({
  selector: 'app-person-detail',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.css']
})
export class PersonDetailComponent {

  @Input() newP!: IPerson;
  x = {} as IPerson;

  // displayModal!: boolean;
  // @Output() newPersonEvent = new EventEmitter<Person>();

  // @Output() newNameEvent = new EventEmitter<string>();
  // newP: Person | undefined;
  // person = {} as Person | undefined;

  // addNewPerson(newPerson: Person) {
  //   this.newPersonEvent.emit(newPerson);
  // }

  constructor(
    private route: ActivatedRoute, 
    private personService: PersonService, 
    private location: Location
  ) { }

  // @ViewChild('childModal') childModal!: Directive;

  ngOnInit(): void {
    this.getPerson();
  }

  getPerson(): void {
    const id = this.route.snapshot.params['id'];
    // console.log(id);
    this.personService.getPerson(id)
      .subscribe(person => {
        this.x = person;
        console.log(this.x);
        console.log(JSON.stringify(person));
      });
  }

  // ngDoCheck() {
  //   this.showChildModal();
  // }

  // showChildModal(): void {
  //   if (this.personService.childModal == true) {
  //     this.childModal
  //   }
  // }

  // showModalDialog() {
  //   this.displayModal = true;
  // }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    if (this.newP) {
      this.personService.updatePerson(this.newP._id, this.newP).subscribe(() => this.goBack())
    }
  }

}
