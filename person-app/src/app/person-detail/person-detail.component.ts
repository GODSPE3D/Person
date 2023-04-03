import { Component, Input, Output, EventEmitter, DoCheck, TemplateRef, ViewChild, Directive, HostListener } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { MessageService } from 'primeng/api';

import { FormControl, Validators } from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';
import { Person, PersonColumns, P } from '../person';
import { PersonService } from '../person.service';
import { MatDialog, MatDialogConfig, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-person-detail, [app-person-detail]',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.css'],
  providers: [MessageService]
})
export class PersonDetailComponent {
  
  @Input() x = {} as Person;
  @ViewChild('addP') customDialog!: TemplateRef<any>;
  @ViewChild('editPerson') customDialog2!: TemplateRef<any>;

  visible!: boolean;
  newP = {} as Person;
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);

  constructor(
    private route: ActivatedRoute, private personService: PersonService, private messageService: MessageService, private location: Location, private dialog: MatDialog
  ) { }

  ngOnInit(): void {
    // this.getPerson();
  }
  
  openDialog() {
    this.dialog.open(this.customDialog);
  }

  openDialog2() {
    this.dialog.open(this.customDialog2);
  }

  // getPerson(): void {
  //   // const id = parseInt(this.route.snapshot.paramMap.get("id")!, 10);
  //   this.personService.getPerson(this.newP._id)
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
