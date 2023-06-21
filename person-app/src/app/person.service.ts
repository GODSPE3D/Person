import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';

import { Person } from './person';
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  private personUrl = 'http://127.0.0.1:5000/person';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }

  getAll(): Observable<Person[]> {
    return this.http.get<Person[]>(this.personUrl);
  }

  getPerson(id: number): Observable<Person> {
    return this.http.get<Person>(this.personUrl + `/${id}`);
  }

  postMail(firstname: string, lastname: string, email: string): Observable<User> {
    return this.http.post<User>(this.personUrl + '/login', {firstname, lastname, email}, this.httpOptions);
  }

  getMail(): Observable<Person> {
    return this.http.get<Person>(this.personUrl + '/login');
  }

  addPerson(person: Person): Observable<Person> {
    return this.http.post<Person>(this.personUrl, person, this.httpOptions);
  }

  deletePerson(id: number) {
    return this.http.delete(this.personUrl + `/` + id, { responseType: 'text' });
  }

  updatePerson(person: Person): Observable<Person> {
    return this.http.put<Person>(this.personUrl + `/${person._id}`, person, this.httpOptions);
  }
}