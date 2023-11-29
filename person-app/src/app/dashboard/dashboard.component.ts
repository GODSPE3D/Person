import { Component, ViewChild } from '@angular/core';
import { KeycloakService } from 'keycloak-angular';

import { ActivatedRoute } from '@angular/router';
import { Person } from '../person';
import { PersonService } from '../person.service';
import { User } from '../user';
import { PersonListComponent } from '../person-list/person-list.component';
import { PersonDetailComponent } from '../person-detail/person-detail.component';
// import { NgbCollapseModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {

  home!: boolean;
  detail!: boolean;
  public isCollapsed = true;
  player!: boolean;
  admin!: boolean;
  manager!: boolean;
  loginStatus!: boolean;
  button = 'home';

  public email: any;
  public firstname: any;
  public lastname: any;

  user = {} as User;
  newPerson = {} as Person;

  @ViewChild(PersonListComponent) child!: PersonListComponent;
  @ViewChild(PersonDetailComponent) child2!: PersonDetailComponent;

  constructor(private readonly keycloak: KeycloakService, private personService: PersonService, private route: ActivatedRoute) {
    this.player = this.keycloak.isUserInRole("player");
    this.admin = this.keycloak.isUserInRole("Admin");
  }

  ngOnInit() {
    this.key();
    // this.getOne();
    this.personService.isLoggedIn.subscribe((status) => {
      this.loginStatus = status;
    });
    // this.child2.ngdirectSwitch = this.button;
  }

  onSelect(button: string) {
    if (button === 'detail') {
      this.button = button;
      this.child2.ngdirectSwitch = this.button;
      // this.detail = true;
      // this.child2.home = false;
    }
    if (button === 'home') {
      this.button = button;
      this.child2.ngdirectSwitch = this.button;
      // this.home = true;
      // this.child2.home = true;
    }
    if (button === 'admin') {
      this.button = button;
      // this.child2.ngdirectSwitch = button;
      // this.detail = true;
      // this.child2.home = false;
    }
  }

  loginSession() {
    this.keycloak.login();
  }

  // login() {
  //   this.personService.loginUser();
  // }

  logoutSession() {
    this.keycloak.logout();
  }

  logout() {
    this.personService.logoutUser();
  }

  buttonCheck() {
    const buttons = Array.from(document.getElementsByClassName('btn'));

    buttons.forEach(btn => {
      btn.addEventListener('click', function handleClick(event) {
        console.log('button clicked');
        console.log(event);
        console.log(event.target);
      });
    });
  }

  // getOne() {
  //   this.personService.email.replace('', 'aeonflux@gmail.com');
  //   // this.personService.postMail().subscribe(newValue => {
  //   //   console.log("dashboard", newValue);
  //   //   this.x = newValue;
  //   // });
  // }

  async key() {
    const currentUser = await this.keycloak.loadUserProfile();

    this.firstname = currentUser.firstName;
    // this.lastname = currentUser.lastName;
    // this.email = currentUser.email;

    this.personService.loginUser();
    this.personService.postMail(currentUser.email as string).subscribe(newP => {
      this.newPerson = newP;
      console.log(this.newPerson);
    });
  }

  // getOne(firstName: string, lastName: string, email: string) {
  //   this.personService.postMail(JSON.stringify({"firstname": firstName}), JSON.stringify({"lastname": lastName}), JSON.stringify({"email": email})).subscribe(newP => {
  //     this.newP = newP;
  //     // this.x = this.newP;
  //     console.log(this.newP);
  //   });
  // }
}
