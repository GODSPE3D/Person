import { Component, OnInit, Input } from '@angular/core';
import { Location } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

import { User } from '../user';
import { UserService } from '../user.service';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})

export class UserListComponent implements OnInit {

  // @Input() user!: User;
  // users: User[] = [];
  p: User[] = [];

  private http = HttpClient;
  constructor(private route: ActivatedRoute, private userService: UserService, private location: Location) { }

  ngOnInit(): void {
    this.userService.getUsers().subscribe((data: any) => {
      this.p = data;
    });
    // this.getUser();
    // this.sayHi();
  }

  // getUsers(): void {
  //   this.userService.getUsers().subscribe(users => this.users = users);
  //   // console.log(this.users)
  // }

  sayHi(user: User): void {
    this.http.get('http://localhost:5000/person').subscribe((data: any) => {
      data as JSON;
      console.log(data)
    })
  //   this.userService.sayHi(user).subscribe(users => this.users = users);
  //   // this.userService.sayHi().subscribe((users: any) => console.log(users));
  //   // this.userService.sayHi().subscribe(data => this.users = users);
  // }


  // getUser(): void {
  //   const id = + this.route.snapshot.paramMap.get('id')
  //   this.userService.getUser(id).subscribe(user => this.user = user);
  // }

  // delete(user: User): void {
  //   this.userService.deleteUser(user).subscribe(success => { this.getUsers(); });
  // }
}
}
