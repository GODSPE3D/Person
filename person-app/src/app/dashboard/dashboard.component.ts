import { Component, ViewChild } from '@angular/core';
import { KeycloakService } from 'keycloak-angular';

import { PersonService } from '../person.service';
import { Person } from '../person';
import { User } from '../user';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { JsonPipe } from '@angular/common';
import { map } from 'rxjs';
import { PersonDetailComponent } from '../person-detail/person-detail.component';

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
  // newPerson = {} as Person;
  // x = <Person>{};
  x = {} as Person;
  person: Person[] = [];
  newP1!: string;
  newP2!: any;

  constructor(private readonly keycloak: KeycloakService, private personService: PersonService, private route: ActivatedRoute) {
    this.player = this.keycloak.isUserInRole("player");
    this.admin = this.keycloak.isUserInRole("Admin");
  }

  ngOnInit() {
    this.key();
    this.getOne();
    //  this.personService.isLoggedIn.subscribe((status) => {
    //   this.loginStatus = status;
    // });
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

  getOne() {
    this.personService.email.replace('', 'aeonflux@gmail.com');
    // this.personService.postMail().subscribe(newValue => {
    //   console.log("dashboard", newValue);
    //   this.x = newValue;
    // });
  }

  async key() {
    const currentUser = await this.keycloak.loadUserProfile();
    
    // this.firstname = currentUser.firstName;
    // this.lastname = currentUser.lastName;
    // this.email = currentUser.email;
    
    this.personService.loginUser();
    this.personService.postMail().subscribe(newP => {
      // this.x = newP;
      console.log("newP", newP);
      // this.x = this.personService.email;
      // this.personService.
      console.log(this.x)
    });
    // console.log(this.child.x);

    // this.personService.postMail(this.firstname, this.lastname, this.email).subscribe(newP => {
      // return {
      // }
      // newP}
      // this.x = newP
      // console.log("x", this.x)
      // console.log("newP", newP)
      // console.log(this.x);
      // console.log(`this.newPerson as Person`, this.newPerson)
      // console.log(`this.newPerson as Person ${this.newPerson.id}`)
      // console.log("this.newPerson as Object values", Object.values(this.newPerson)["0"]["id"])
      // console.log("this.newPerson as JSON", JSON.parse(JSON.stringify(this.newPerson)))
      // this.personService.getPerson(Object.values(this.x)["0"]["id"]).subscribe(x => {
      //   this.x = x
      //   console.log("x", this.x)
      // });
    // });
  }

  // getOne(firstName: string, lastName: string, email: string) {
  //   this.personService.postMail(JSON.stringify({"firstname": firstName}), JSON.stringify({"lastname": lastName}), JSON.stringify({"email": email})).subscribe(newP => {
  //     this.newP = newP;
  //     // this.x = this.newP;
  //     console.log(this.newP);
  //   });
  // }
}
