import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { map, Observable, tap } from 'rxjs';
import { IPerson } from './person';

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  childModal!: Boolean;
  private personUrl = 'http://127.0.0.1:5000/person';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }

  // public getPerson(): Observable<Person[]> {
  //   return this.http.get<Person[]>(this.personUrl);
  // }

  // public addPerson(singlePerson: Person): Observable<Person> {
  //   return this.http.post<Person>(this.personUrl, singlePerson);
  // }

  getPersonAll(): Observable<IPerson[]> {
    return this.http.get<IPerson[]>(this.personUrl);
  }

  getPerson(id: number): Observable<IPerson> {
    const url = `${this.personUrl}/${id}`;
    return this.http.get<IPerson>(url).pipe(map((p: IPerson) => p));
  }

  addPerson(p: IPerson): Observable<IPerson> {
    return this.http.post<IPerson>(this.personUrl, p);
  }

  deletePerson(id: number): Observable<IPerson> {
    const url = `${this.personUrl}/${id}`;

    return this.http.delete<IPerson>(url, this.httpOptions);
  }

  updatePerson(id: number, p: IPerson): Observable<IPerson> {
    const url = `${this.personUrl}/${id}`;
    return this.http.put<IPerson>(url, p, this.httpOptions);
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
