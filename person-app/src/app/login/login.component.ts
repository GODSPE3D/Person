import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { User } from '../user';
import { PersonService } from '../person.service';
import { LoginService } from '../login.service';
import { KeycloakService } from 'keycloak-angular';
import { KeycloakProfile, KeycloakRoles } from 'keycloak-js';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  loading = false;
  submitted = false;
  returnUrl!: string;
  user = {} as User;
  public isLogged = false;
  public userProfile: KeycloakProfile | null = null;

  constructor(private formBuilder: FormBuilder, private route: ActivatedRoute, private router: Router, private loginService: LoginService, private readonly keycloak: KeycloakService) {}

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
}
