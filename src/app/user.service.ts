import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { User } from './user';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({ providedIn: 'root' })
export class UserService {

  private userUrl = 'http://localhost:5000';  // URL to REST API

  constructor(private http: HttpClient) { }

//   private static _handleError(err: HttpErrorResponse | any) {
//     return Observable.
//   }

  /** GET users from the server */
  // getUsers(): Observable<User[]> {
  //   return this.http.get<User[]>(this.userUrl + '/person');
  //   // console.log(user);
  // }

  public getUsers() {
    return this.http.get<User[]>(this.userUrl + '/person/');
  }

  // sayHi() {
  //   this.http.get(this.userUrl + '/person').pipe(map(data => {}))
  // }

  // sayHi(): Observable<User[]> {
  //   return this.http.get(this.userUrl + '/person').pipe(map((result: any) => result.json()))
  // }

  // sayHi(user: User) {
  //   return this.http.get<User[]>(this.userUrl + '/person');
  // }
  
//   /** GET user by id. Will 404 if id not found */
//   getUser(id: number): Observable<any> {
//     const url = `${this.userUrl}/person/${id++}`;
//     return this.http.get<User>(url);
//   }
  
//   /** POST: add a new user to the server */
//   addUser(user: User) {
// 	//console.log(user);
//     return this.http.post(this.userUrl + '/add', user, httpOptions);
//   }
  
//   /** PUT: update the user on the server */
//   updateUser(user: User): Observable<any> {
//     return this.http.put(this.userUrl + '/update', user, httpOptions);
//   }
  
  /** DELETE: delete the user from the server */
  deleteUser(user: User | number) {
	  if (confirm("Are you sure to delete?")) {
		const id = typeof user === 'number' ? user : user.id;
		const url = `${this.userUrl}/delete/${id}`;
		return this.http.delete(url, httpOptions);
	  }
	  return of({});
  }

}