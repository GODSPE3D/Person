import { Component } from '@angular/core';
import { KeycloakService } from 'keycloak-angular';

import { ActivatedRoute } from '@angular/router';
import { Person } from '../person';
import { PersonService } from '../person.service';
import { User } from '../user';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  // @ViewChild(PersonDetailComponent) child: PersonDetailComponent;

  player!: boolean;
  admin!: boolean;
  manager!: boolean;
  loginStatus!: boolean;
  
  public email: any;
  public firstname: any;
  public lastname: any;

  user = {} as User;
  newPerson = {} as Person;

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
