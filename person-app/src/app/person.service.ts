import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { BehaviorSubject, Observable, map } from 'rxjs';

import { Contact, Person } from './person';
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  isLoggedIn = new BehaviorSubject(false);

  logoutUser() {
    this.isLoggedIn.next(false);
  }
  
  loginUser() {
    this.isLoggedIn.next(true);
  }

  private personUrl = 'http://127.0.0.1:5000/person';
  email = '';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };

  constructor(private http: HttpClient) { }

  getAll(): Observable<Person[]> {
    return this.http.get<Person[]>(this.personUrl);
  }

  getPerson(id: number): Observable<Person> {
    return this.http.get<Person>(`${this.personUrl}/${id}`);
  }

  // postMail(firstname: string, lastname: string, email: string): Observable<Person> {
  //   // return this.http.get<Person>(`${this.personUrl}/login`);
  //   return this.http.post<Person>(`${this.personUrl}/login`, {firstname, lastname, email}, this.httpOptions);
  // }

  postMail(): Observable<Person> {
    // this.email = email;
    // return this.http.post<Person>(`${this.personUrl}/login`, {email: "aeonflux@gmail.com"}, this.httpOptions)
    return this.http.get<Person>(`${this.personUrl}/login`).pipe();
    // this.http.get('...').map(res => <Product[]>res.json());
    // return this.http.post<Person>(`${this.personUrl}/login`, {firstname: "Aeon", lastname: "Flux", email: "aeonflux@gmail.com"}, this.httpOptions)
    // return this.http.post<Person>(`${this.personUrl}/login`, {firstname: "Aeon", lastname: "Flux", email: "aeonflux@gmail.com"}, this.httpOptions)
  }

  public set value(v : string) {
    this.email = v;
  }

  get value() : string {
    return this.email;
  }
  
  addPerson(person: Person): Observable<Person> {
    return this.http.post<Person>(this.personUrl, person, this.httpOptions);
  }

  deletePerson(id: number) {
    return this.http.delete(`${this.personUrl}/${id}`, { responseType: 'text' });
  }

  updatePerson(person: Person): Observable<Person> {
    return this.http.put<Person>(this.personUrl + `/${person.id}`, person, this.httpOptions);
  }
}