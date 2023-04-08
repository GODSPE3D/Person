import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { map, Observable, tap, catchError, of } from 'rxjs';
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

  getPerson(id: number): Observable<Person> {
    return this.http.get<Person>(this.personUrl + `/${id}`);
  }

  addPerson(p: Person): Observable<Person> {
    return this.http.post<Person>(this.personUrl, p, this.httpOptions);
  }

  deletePerson(id: number): Observable<Person> {
    return this.http.delete<Person>(this.personUrl + `/${id}`, this.httpOptions);
  }

  updatePerson(p: Person): Observable<Person> {
    return this.http.put<Person>(this.personUrl + `/${p._id}`, p, this.httpOptions);
  }
}
