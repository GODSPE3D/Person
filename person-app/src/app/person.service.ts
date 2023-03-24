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

  getPersonAll(): Observable<Person[]> {
    return this.http.get<Person[]>(this.personUrl);
  }

  getPerson(id: number): Observable<Person[]> {
    const url = `${this.personUrl}/${id}`;
    return this.http.get<Person[]>(url);
  }

  addPerson(p: Person): Observable<Person> {
    return this.http.post<Person>(this.personUrl, p);
  }

  deletePerson(id: number): Observable<Person> {
    const url = `${this.personUrl}/${id}`;

    return this.http.delete<Person>(url, this.httpOptions);
  }

  updatePerson(id: number, p: Person): Observable<Person> {
    const url = `${this.personUrl}/${id}`;
    return this.http.put<Person>(url, p, this.httpOptions);
  }
}
