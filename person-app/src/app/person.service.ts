import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { map, Observable, tap } from 'rxjs';
import { Person } from './person';

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  private personUrl = 'http://127.0.0.1:5000/person';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }

  // public getPerson(): Observable<Person[]> {
  //   return this.http.get<Person[]>(this.personUrl);
  // }

  // getPer(id: number): Observable<Person> {
  //   return this.http.get<Person>(this.personUrl + `/${id}`);
  // }

  // public addPerson(singlePerson: Person): Observable<Person> {
  //   return this.http.post<Person>(this.personUrl, singlePerson);
  // }

  getPerson(): Observable<Person[]> {
    return this.http.get<Person[]>(this.personUrl);
  }

  addPerson(p: Person): Observable<Person> {
    return this.http.post<Person>(this.personUrl, p);
  }

  deletePerson(id: number): Observable<Person> {
    const url = `${this.personUrl}/${id}`;

    return this.http.delete<Person>(url, this.httpOptions);
  }

  updatePerson(p: Person): Observable<any> {
    return this.http.put(this.personUrl, p, this.httpOptions);
  }

  // getP(id: number): Observable<Person> {
  //   const url = `${this.personUrl}/${id}`;
  //   return this.http.get<Person>(url);
  // }

  // deletePerson(id: number): Observable<Person> {
  //   const url = `${this.personUrl}/${id}`;

  //   return this.http.delete<Person>(url, this.httpOptions).pipe()
  // }
  

  // GetUser(id: number): Observable<Person[]> {
  //   return this.http.get<Person[]>(this.personUrl + 'person' + id.toString());
  // }
}
