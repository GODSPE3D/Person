import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { map, Observable } from 'rxjs';
import { Person } from './person';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  private personUrl = 'http://127.0.0.1:5000/';

  constructor(private http: HttpClient) { }

  public getPerson() {
    return this.http.get<Person[]>(this.personUrl + 'person');
  }

  // GetUser(id: number): Observable<Person[]> {
  //   return this.http.get<Person[]>(this.personUrl + 'person' + id.toString());
  // }
}
