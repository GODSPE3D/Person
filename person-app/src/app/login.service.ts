import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private loginUrl = 'http://127.0.0.1:5000/person';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }

  get_login(): Observable<User> {
    return this.http.get<User>(this.loginUrl + `/login`);
  }

  login(username: string, password: string): Observable<User> {
    return this.http.post<User>(this.loginUrl, { username, password }, this.httpOptions);
  }
}
