import { Component, Input, Output, EventEmitter, TemplateRef, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { User } from '../user';
import { FormControl, Validators } from '@angular/forms';
import { Person } from '../person';
import { PersonService } from '../person.service';
import { LoginService } from '../login.service';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { KeycloakService } from 'keycloak-angular';
import { KeycloakProfile } from 'keycloak-js';

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

  public isLogged = false;
  public userProfile: KeycloakProfile | null = null;

  user = {} as User;

  newP = {} as Person;
  @Output() addP = new EventEmitter<Person>();
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);

  constructor(
    private route: ActivatedRoute, private loginService: LoginService, private readonly keycloak: KeycloakService, private personService: PersonService, private location: Location, private dialog: MatDialog, private _snackBar: MatSnackBar
  ) { }

  @Output() delEvent = new EventEmitter();

  public async ngOnInit() {
      // this.loginForm = this.formBuilder.group({
      //   username: ['', Validators.required],
      //   password: ['', Validators.required]
      // })
      this.getLog();
      this.isLogged = await this.keycloak.isLoggedIn();
      if (this.isLogged) {
        this.userProfile = await this.keycloak.loadUserProfile();
      }
      console.log(this.userProfile);
      this.user = this.userProfile as User;
  }

  getLog(): void {
    this.loginService.get_login().subscribe();
  }

  loginPerson(user: User): void {
    console.log(user. username, user.password);
    this.loginService.login(user.username, user.password).subscribe();
  }

  public loginSession() {
    this.keycloak.login();
  }

  public logoutSession() {
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