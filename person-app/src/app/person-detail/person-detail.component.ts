import { Component, Input, Output, EventEmitter, TemplateRef, ViewChild, OnChanges, SimpleChanges, ChangeDetectorRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { User } from '../user';
import { FormControl, Validators } from '@angular/forms';
import { Contact, Person } from '../person';
import { PersonService } from '../person.service';
import { LoginService } from '../login.service';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { KeycloakEventType, KeycloakService } from 'keycloak-angular';
import { KeycloakProfile } from 'keycloak-js';
import { from, filter } from 'rxjs';

@Component({
  selector: 'app-person-detail, [app-person-detail]',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.css'],
  providers: []
})
export class PersonDetailComponent {

  @Input() x = {} as Person;
  // @Input() x1!: Person;
  // myDataCopy = {...this.x};
  dataVar!: boolean;

  @ViewChild('addP') customDialog!: TemplateRef<any>;
  @ViewChild('editPerson') customDialog2!: TemplateRef<any>;

  public isLogged = false;
  public userProfile: KeycloakProfile | null = null;

  @Input() user!: User;
  public email: any;

  // p: Person[] = [];
  public p: Person = {
    id: 0,
    firstname: '',
    lastname: '',
    email: '',
    contact: [],
    address: [],
    education: '',
    password: ''
    // aadhaar: 1
  }
  newP = {} as Person;
  single = {} as Person;
  @Output() addP = new EventEmitter<Person>();
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);
  changeLog: any;

  constructor(
    private cdr: ChangeDetectorRef, private route: ActivatedRoute, private loginService: LoginService, private readonly keycloak: KeycloakService, private personService: PersonService, private location: Location, private dialog: MatDialog, private _snackBar: MatSnackBar
  ) {
    // this.player = this.keycloak.isUserInRole("player");
  }

  @Output() delEvent = new EventEmitter();

  ngOnInit() {
    this.getOne();
    // console.log(this.route.snapshot.paramMap.get('5'));
    // this.key();
    // console.log(this.x.firstname);

    // console.log(this.myDataCopy.firstname);
    // this.ngOnChanges;
    // this.loginForm = this.formBuilder.group({
    //   username: ['', Validators.required],
    //   password: ['', Validators.required]
    // })
    // this.x = this.newP;
    // console.log(this.newP.firstname);
    // this.getLog();
    // this.isLogged = await this.keycloak.isLoggedIn();
    // if (this.isLogged) {
    //   let userProfile = await this.keycloak.loadUserProfile();
    //   // console.log(this.userProfile);
    //   // this.email = userProfile.email;
    //   // console.log(this.email);
    // }

    // this.user = this.userProfile as User;
    // this.p.forEach((a) => {
    //   if (this.user.email == a.email) {
    //     console.log('' + a.email);
    //   }
    //   console.log(a.email);
    // })
    // from(this.keycloak.keycloakEvents$)
    // .pipe(filter(event => event.type === KeycloakEventType.OnTokenExpired))
    // .subscribe(() => console.log('The token has expired', this.keycloak.logout()))
    // console.dir(this.x);

    // if (this.keycloak.isTokenExpired(this.keycloak.getToken()) === true) {
    //   this.logoutSession();
    // };
    // this.getOne();
    // this.newP = this.x;
    // console.log("detail ", this.x);
    // console.log("User: ", this.user);
  }
  
  // changeLog: string[] = [];

  // ngOnChanges(changes: SimpleChanges) {
  //   const log: string[] = [];
  //   for (const propName in changes) {
  //     const changedProp = changes[propName];
  //     const to = JSON.stringify(changedProp.currentValue);
  //     if (changedProp.isFirstChange()) {
  //       log.push(`Initial value of ${propName} set to ${to}`);
  //     } else {
  //       const from = JSON.stringify(changedProp.previousValue);
  //       log.push(`${propName} changed from ${from} to ${to}`);
  //     }
  //   }
  //   // this.changeLog.push(log.join(', '));
  // }

  // ngOnChanges(changes: SimpleChanges) {
  //   for (const propName in changes) {
  //     const chng = changes[propName];
  //     const cur  = JSON.stringify(chng.currentValue);
  //     const prev = JSON.stringify(chng.previousValue);
  //     this.changeLog.push(`${propName}: currentValue = ${cur}, previousValue = ${prev}`);
  //   }
  // }


  // async key() {
  //   let currentUser = await this.keycloak.loadUserProfile();
  //   this.user.firstname = currentUser.firstName as string;
  //   this.user.lastname = currentUser.lastName as string;
  //   this.user.email = currentUser.email as string;
  //   // console.log(currentUser);
  //   console.log("User: ", this.user);
  //   return this.user;
  //   // this.getOne(currentUser.email as string);
  // }

  getLog(): void {
    this.loginService.get_login().subscribe();
  }

  getOne() {
    this.personService.getPerson(5).subscribe(newValue => {
      // let p: Person = {
      //   id: 0,
      //   firstname: '',
      //   lastname: '',
      //   email: '',
      //   contact: [],
      //   address: [],
      //   education: '',
      //   password: ''
      //   // aadhaar: 1
      // }

      this.newP = newValue;
      console.log('p -> ', this.newP);
      // this.newP = newValue;
      // console.log(this.newP);
      // this.cdr.detectChanges();
    });
  }

  // loginPerson(user: User): void {
  //   console.log(user. username, user.password);
  //   this.loginService.login(user.username, user.password).subscribe();
  // }

  public async loginSession() {
    this.keycloak.login();
    console.log(this.email);
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
    if (this.x) {
      this.personService.updatePerson(this.x).subscribe();
    }
  }

  // deletePerson(delP: Person): void {
  //   this.personService.deletePerson(delP.id).subscribe(person => {
  //     console.log(person);
  //     // this.x = person
  //     this.delEvent.emit(this.x);
  //   });
  // }
}