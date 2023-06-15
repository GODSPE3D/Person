import { Component, Input, Output, EventEmitter, TemplateRef, ViewChild, OnChanges, SimpleChanges } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { User } from '../user';
import { FormControl, Validators } from '@angular/forms';
import { Person } from '../person';
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
  // myDataCopy = {...this.x};
  player!: boolean;

  @ViewChild('addP') customDialog!: TemplateRef<any>;
  @ViewChild('editPerson') customDialog2!: TemplateRef<any>;

  public isLogged = false;
  public userProfile: KeycloakProfile | null = null;

  @Input() user = {} as User;
  public email: any;

  newP = {} as Person;
  single = {} as Person;
  @Output() addP = new EventEmitter<Person>();
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);

  constructor(
    private route: ActivatedRoute, private loginService: LoginService, private readonly keycloak: KeycloakService, private personService: PersonService, private location: Location, private dialog: MatDialog, private _snackBar: MatSnackBar
  ) {
    this.player = this.keycloak.isUserInRole("player");
  }

  @Output() delEvent = new EventEmitter();

  ngOnInit() {
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
      console.log(this.x);
      console.log("User: ", this.user);
  }

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

  getOne(email: string) {
    // this.personService.postMail(JSON.stringify({"email": email})).subscribe(newPe => {
    //   this.newP.email = email;
    //   this.newP = newPe;
    //   // this.x = this.newP;
    //   console.log(this.newP);
    //   // this.personService.getPerson(this.newP._id).subscribe(single => {
    //   //   this.single = single;
    //   //   console.log(this.single);
    //   // })
    // });
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

  // getOne(): void {
  //   if (this.user.firstName === this.x.firstname) {
  //     this.personService.getPerson(this.x._id).subscribe(p => this.p = p);
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

  deletePerson(delP: Person): void {
    this.personService.deletePerson(delP._id).subscribe(person => {
      console.log(person);
      // this.x = person
      this.delEvent.emit(this.x);
    });
  }
}