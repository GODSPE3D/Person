import { Component, Input, Output, EventEmitter, DoCheck, TemplateRef, ViewChild, Directive, HostListener } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { MessageService } from 'primeng/api';

import { FormControl, Validators } from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';
import { Person } from '../person';
import { PersonService } from '../person.service';
import { MatDialog, MatDialogConfig, MatDialogRef } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';

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

  newP = {} as Person;
  @Output() outP = new EventEmitter<Person>();
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);

  constructor(
    private route: ActivatedRoute, private personService: PersonService, private messageService: MessageService, private location: Location, private dialog: MatDialog, private _snackBar: MatSnackBar
  ) { }

  @Output() delEvent = new EventEmitter();

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
  //   this.newP = this.x;
  //   const id = parseInt(this.route.snapshot.paramMap.get('id')!, 10);
  //   this.personService.getPerson(id)
  //     .subscribe(hero => this.x = hero);
  // }

  addPerson(newP: Person) {
    // john
    // does
    // john@doe.com
    // 1234567896
    // India
    // PhD
    // password
    // 123245685464

    // console.log(this.newP);
    // this.personService.addPerson(this.newP).subscribe();
    // this.personService.getPersonAll();
    this.personService.addPerson(newP).subscribe();
    this.outP.emit(newP);
  }

  goBack(): void {
    this.location.back();
  }

  // editPerson(newP: Person) {
  //     // this.personService.updatePerson(person._id, person).subscribe(() => person.isEdit = false);
  //     newP = this.x;
  //     if (newP._id == null) {
  //       this.personService.addPerson(newP).subscribe((newPerson: Person) => {
  //         newP._id = newPerson._id;
  //         // newP.isEdit = false;
  //       });
  //     } else {
  //       this.personService.updatePerson(newP._id, newP).subscribe();
  //     }
  //   }

  save(): void {
    // this.newP = this.x;
    if (this.x) {
      this.personService.updatePerson(this.x).subscribe();
      // this._snackBar.open('Profile updated', 'Close', {
      //   horizontalPosition: 'right',
      //   verticalPosition: 'top',
      //   duration: 4000,
      //   panelClass: ['green-snack']
      // });
      // this.messageService.add({ severity: 'success', summary: 'Success', detail: 'Updated successfully!' });
    }
  }

  deletePerson(delP: Person): void {
    // if (this.newP._id = id) {
      // this.personService.deletePerson(delP._id).subscribe(() => {
      //   this.personService.getPersonAll().subscribe();
      // });
    // }
    // this.x = this.x; 
    
    // console.log(delP);
    // this.personService.deletePerson(delP._id).subscribe();
    // this.personService.getPersonAll().subscribe();
    // console.log("successful");
    // this.personService.deletePerson(delP._id).subscribe(result => {
    //   console.log(result);
    //   this.delEvent.emit(this.personService.getPersonAll());
    // })

    this.personService.deletePerson(delP._id).subscribe(person => {
      console.log(person);
      this.x = person
      this.delEvent.emit(this.x);
    });
    // if(confirm("Are you sure to delete the project?")) {
    //   this.personService.deletePerson(id)
    //     .subscribe(result =>{        
    //      if(result.status == 204){
    //        console.log('removed');
    //        this.someEvent.emit(null);
    //      };
    //    }); 
    // } 
  }
}
