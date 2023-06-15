import { Component } from '@angular/core';
import { KeycloakService } from 'keycloak-angular';

import { PersonService } from '../person.service';
import { Person } from '../person';
import { User } from '../user';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  player!: boolean;
  manager!: boolean;
  
  public email: any;
  public firstname: any;
  public lastname: any;

  newP = {} as User;
  newP1!: string;
  newP2!: any;

  constructor(private readonly keycloak: KeycloakService, private personService: PersonService) {
    this.player = this.keycloak.isUserInRole("player");
  }

  ngOnInit() {
    this.key();
  }

  loginSession() {
    this.keycloak.login();
  }

  async key() {
    let currentUser = await this.keycloak.loadUserProfile();
    this.firstname = currentUser.firstName;
    this.lastname = currentUser.lastName;
    this.email = currentUser.email;
    console.log(currentUser);
    // this.getOne(currentUser.firstName as string, currentUser.lastName as string, currentUser.email as string);
    this.personService.postMail(this.firstname, this.lastname, this.email).subscribe(newP => {
      console.log(newP)
      this.newP = newP
      // console.log(this.newP)
    });
    // this.personService.getMail(this.firstName, this.lastName, this.email).subscribe(newP => {
    //   this.newP = newP;
    //   // this.x = this.newP;
    //   console.log(this.newP);
    // });
  }

  // getOne(firstName: string, lastName: string, email: string) {
  //   this.personService.postMail(JSON.stringify({"firstname": firstName}), JSON.stringify({"lastname": lastName}), JSON.stringify({"email": email})).subscribe(newP => {
  //     this.newP = newP;
  //     // this.x = this.newP;
  //     console.log(this.newP);
  //   });
  // }

  logoutSession() {
    this.keycloak.logout();
  }
}
