import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { User } from '../user';
import { PersonService } from '../person.service';
import { LoginService } from '../login.service';

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

  constructor(private formBuilder: FormBuilder, private route: ActivatedRoute, private router: Router, private loginService: LoginService) {}

  ngOnInit(): void {
      // this.loginForm = this.formBuilder.group({
      //   username: ['', Validators.required],
      //   password: ['', Validators.required]
      // })
      this.getLog();
  }

  getLog(): void {
    this.loginService.get_login().subscribe();
  }

  loginPerson(user: User): void {
    console.log(user. username, user.password);
    this.loginService.login(user.username, user.password).subscribe();
  }
}
