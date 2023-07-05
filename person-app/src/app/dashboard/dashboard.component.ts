import { Component } from '@angular/core';
import { KeycloakService } from 'keycloak-angular';

import { PersonService } from '../person.service';
import { Person } from '../person';
import { User } from '../user';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { JsonPipe } from '@angular/common';
import { map } from 'rxjs';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  player!: boolean;
  admin!: boolean;
  manager!: boolean;
  loginStatus!: boolean;
  
  public email: any;
  public firstname: any;
  public lastname: any;

  user = {} as User;
  newPerson = {} as Person;
  x = {} as Person;
  newP1!: string;
  newP2!: any;

  constructor(private readonly keycloak: KeycloakService, private personService: PersonService, private route: ActivatedRoute) {
    this.player = this.keycloak.isUserInRole("player");
    this.admin = this.keycloak.isUserInRole("Admin");
  }

  ngOnInit() {
    this.key();
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

  async key() {
    const currentUser = await this.keycloak.loadUserProfile();
    // return currentUser;
    this.firstname = currentUser.firstName;
    this.lastname = currentUser.lastName;
    this.email = currentUser.email;
    console.log(currentUser);

    this.user.firstname = currentUser.firstName as string;
    this.user.lastname = currentUser.lastName as string;
    this.user.email = currentUser.email as string;
    console.log('user', this.user);

    this.personService.postMail(this.firstname, this.lastname, this.email).subscribe(newP => {
      console.log("newP", newP)
      this.newPerson = newP;
      
      this.personService.loginUser();

      console.log(`this.newPerson as Person`, this.newPerson)
      console.log(`this.newPerson as Person ${this.newPerson._id}`)
      console.log("this.newPerson as Object values", Object.values(this.newPerson)["0"]["_id"])
      console.log("this.newPerson as JSON", JSON.parse(JSON.stringify(this.newPerson)))

      // this.personService.getPerson(newP._id).pipe(map())
      // });

      this.personService.getPerson(Object.values(this.newPerson)["0"]["_id"]).subscribe(x => {
        this.x = x
        console.log("x", this.x)
      });
      // this.personService.getPerson(Object.values(this.newPerson)["0"]["_id"]).subscribe(x => {
      //   this.x = x
      //   console.log("x", this.x)
      // });
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
