import { Location } from '@angular/common';
import { ChangeDetectorRef, Component, EventEmitter, Input, Output, TemplateRef, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { FormControl, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { KeycloakService } from 'keycloak-angular';
import { KeycloakProfile } from 'keycloak-js';
import { LoginService } from '../login.service';
import { Person, Contact, Address } from '../person';
import { PersonService } from '../person.service';
import { User } from '../user';
import { ModalDismissReasons, NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-person-detail, [app-person-detail]',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.css'],
  providers: []
})
export class PersonDetailComponent {

  @Input() people!: Person;
  @Input() person!: Person;
  @Input() player!: boolean;
  @Input() home!: boolean;
  @Input() detail!: boolean;
  @Input() ngdirectSwitch!: string;

  dataVar!: boolean;

  @ViewChild('addP') customDialog!: TemplateRef<any>;
  @ViewChild('editPerson') customDialog2!: TemplateRef<any>;
  @ViewChild('content') modalNGB!: TemplateRef<any>;
  @ViewChild('detail') detailTemp!: TemplateRef<any>;
  // @ViewChild('home') home!: boolean;

  public isLogged = false;
  public userProfile: KeycloakProfile | null = null;
  agree!: boolean;

  @Input() user!: User;
  public email: any;
  closeResult = '';

  newP = {} as Person;
  single = {} as Person;
  @Output() addP = new EventEmitter<Person>();
  @Output() detailP = new EventEmitter<Person>();
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);
  changeLog: any;

  constructor(private modalService: NgbModal,
    private cdr: ChangeDetectorRef, private route: ActivatedRoute, private loginService: LoginService, private readonly keycloak: KeycloakService, private personService: PersonService, private location: Location, private dialog: MatDialog, private _snackBar: MatSnackBar
  ) {
    // this.player = this.keycloak.isUserInRole("player");
  }

  @Output() delEvent = new EventEmitter();

  ngOnInit() {
  }

  getOne() {
    this.personService.getPerson(5).subscribe(newValue => {

      this.person = newValue;
      console.log('p -> ', this.person);
    });
  }

  openModal() {
    this.modalService.open(this.modalNGB, { ariaLabelledBy: 'modal-basic-title' }).result.then(
      (result) => {
        this.closeResult = `Closed with: ${result}`;
      },
      (reason) => {
        this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
      },
    );
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return `with: ${reason}`;
    }
  }

  logoutSession() {
    this.keycloak.logout();
  }

  public registerUser() {
    this.keycloak.register();
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

  // addContact(newC: Contact) {
  //   this.
  // }

  // getOne(): void {
  //   if (this.user.firstName === this.x.firstname) {
  //     this.personService.getPerson(this.x.id).subscribe(p => this.p = p);
  //   }
  // }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    if (this.people) {
      this.personService.updatePerson(this.people).subscribe();
    }
  }

  deletePerson(delP: Person): void {
    this.personService.deletePerson(delP.id).subscribe(person => {
      console.log(person);
      // this.x = person
      this.delEvent.emit(this.people);
    });
  }
}