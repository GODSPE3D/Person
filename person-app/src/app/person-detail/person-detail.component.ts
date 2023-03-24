import { Component, Input, Output, EventEmitter, DoCheck, ViewChild, Directive } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { MessageService } from 'primeng/api';

import {FormControl, Validators} from '@angular/forms';
import { Person } from '../person';
import { PersonService } from '../person.service';
import { MatDialog, MatDialogConfig, MatDialogRef} from '@angular/material/dialog';

@Component({
  selector: 'app-person-detail',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.css'],
  providers: [MessageService]
})
export class PersonDetailComponent {

  @Input() newP!: Person;
  x = {} as Person;

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
    private messageService: MessageService,
    private location: Location,
    public dialogRef: MatDialogRef<PersonDetailComponent>
  ) { }

  // @ViewChild('childModal') childModal!: Directive;

  ngOnInit(): void {
    // this.getPerson();
  }

  emailFormControl = new FormControl('', [Validators.required, Validators.email]);

  // openDialog(): void {
  //   // const dialogRef = this.dialog.open(PersonListComponent, {
  //   //   // data: {name: this.name, animal: this.animal},
  //   // });

  //   // dialogRef.afterClosed().subscribe(result => {
  //   //   console.log('The dialog was closed');
  //   //   // this.animal = result;
  //   // });

  //   const dialogConfig = new MatDialogConfig();

  //       dialogConfig.disableClose = true;
  //       dialogConfig.autoFocus = true;

  //       this.dialog.open(PersonDetailComponent, dialogConfig);
  // }

  // getPerson(): void {
  //   // const id = this.route.snapshot.params['id'];
  //   const id = parseInt(this.route.snapshot.paramMap.get("id")!, 10);
  //   this.personService.getPerson(id)
  //     .subscribe(p => this.x = p);
  //   console.log(this.x);
  //   // console.log(id);
  //   // this.personService.getPerson(id)
  //   //   .subscribe(person => {
  //   //     this.x = person;
  //   //     console.log('', this.x);
  //   //     // console.log(this.x.prototype.toString());
  //   //     // console.log(this.x[K1]);
  //   //     console.log(JSON.stringify(this.x));
  //   //     console.log(JSON.parse(JSON.stringify(this.x)));
  //   //   });
  // }

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

  // save(): void {
  //   if (this.x) {
  //     this.personService.updatePerson(this.x[0]._id, this.x[0]).subscribe();
  //     this.messageService.add({ severity: 'success', summary: 'Success', detail: 'Updated successfully!' });
  //   }
  // }



}
