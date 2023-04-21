import { Component, Input, Output, EventEmitter, TemplateRef, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { FormControl, Validators } from '@angular/forms';
import { Person } from '../person';
import { PersonService } from '../person.service';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-person-detail, [app-person-detail]',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.css'],
  providers: []
})
export class PersonDetailComponent {

  @Input() x = {} as Person;
  @ViewChild('addP') customDialog!: TemplateRef<any>;
  @ViewChild('editPerson') customDialog2!: TemplateRef<any>;

  newP = {} as Person;
  @Output() addP = new EventEmitter<Person>();
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);

  constructor(
    private route: ActivatedRoute, private personService: PersonService, private location: Location, private dialog: MatDialog, private _snackBar: MatSnackBar
  ) { }

  @Output() delEvent = new EventEmitter();

  ngOnInit(): void {
  }

  openDialog() {
    this.dialog.open(this.customDialog);
  }

  openDialog2() {
    this.dialog.open(this.customDialog2);
  }

  addPerson(newP: Person) {
    // john
    // does
    // john@doe.com
    // 1234567896
    // India
    // PhD
    // password
    // 123245685464
    this.addP.emit(newP);
  }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    if (this.x) {
      this.personService.updatePerson(this.x).subscribe();
    }
  }

  deletePerson(delP: Person): void {
    this.personService.deletePerson(delP._id).subscribe(person => {
      console.log(person);
      // this.x = person
      this.delEvent.emit(this.x);
    });
  }
}