import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { BehaviorSubject, Observable, Subject, debounceTime, delay, switchMap, tap } from 'rxjs';

import { Contact, Person } from './person';

interface SearchResult {
  countries: Person[];
  total: number;
}

interface State {
  page: number;
  pageSize: number;
  searchTerm: string;
}

// const compare = (v1: string | number, v2: string | number) => (v1 < v2 ? -1 : v1 > v2 ? 1 : 0);

// function sort(countries: Person[], column: SortColumn, direction: string): Country[] {
// 	if (direction === '' || column === '') {
// 		return countries;
// 	} else {
// 		return [...countries].sort((a, b) => {
// 			const res = compare(a[column], b[column]);
// 			return direction === 'asc' ? res : -res;
// 		});
// 	}
// }

function matches(country: Person, term: string) {
  return (
    country.firstname.toLowerCase().includes(term.toLowerCase()) ||
    country.lastname.toLowerCase().includes(term.toLowerCase()) ||
    country.email.toLowerCase().includes(term.toLowerCase())
  );
}

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  isLoggedIn = new BehaviorSubject(false);
  
  private _loading$ = new BehaviorSubject<boolean>(true);
	private _search$ = new Subject<void>();
	private _countries$ = new BehaviorSubject<Person[]>([]);
	private _total$ = new BehaviorSubject<number>(0);

  private _state: State = {
		page: 1,
		pageSize: 4,
		searchTerm: '',
	};

  logoutUser() {
    this.isLoggedIn.next(false);
  }

  loginUser() {
    this.isLoggedIn.next(true);
  }

  private personUrl = 'http://127.0.0.1:5000/person';
  private contactUrl = 'http://127.0.0.1:5000/person/contact';
  email = '';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };

  constructor(private http: HttpClient) {
    // this._search$
		// 	.pipe(
		// 		tap(() => this._loading$.next(true)),
		// 		debounceTime(200),
		// 		switchMap(() => this._search()),
		// 		delay(200),
		// 		tap(() => this._loading$.next(false)),
		// 	)
		// 	.subscribe((result) => {
		// 		this._countries$.next(result.countries);
		// 		this._total$.next(result.total);
		// 	});

		// this._search$.next();
  }

  get countries$() {
		return this._countries$.asObservable();
	}
	get total$() {
		return this._total$.asObservable();
	}
	get loading$() {
		return this._loading$.asObservable();
	}
	get page() {
		return this._state.page;
	}
	get pageSize() {
		return this._state.pageSize;
	}
	get searchTerm() {
		return this._state.searchTerm;
	}

	set page(page: number) {
		this._set({ page });
	}
	set pageSize(pageSize: number) {
		this._set({ pageSize });
	}
	set searchTerm(searchTerm: string) {
		this._set({ searchTerm });
	}

  private _set(patch: Partial<State>) {
		Object.assign(this._state, patch);
		this._search$.next();
	}

  // private _search(): Observable<SearchResult> {
		// const { pageSize, page, searchTerm } = this._state;

		// 1. sort
		// let countries = Person;

		// 2. filter
		// countries = countries.filter((country) => matches(country, searchTerm));
		// const total = countries.length;

		// // 3. paginate
		// countries = countries.slice((page - 1) * pageSize, (page - 1) * pageSize + pageSize);
		// return of({ countries, total });
	// }

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

  postMail(email: string): Observable<Person> {
    // this.email = email;
    // return this.http.post<Person>(`${this.personUrl}/login`, {email: "aeonflux@gmail.com"}, this.httpOptions)
    // return this.http.get<Person>(`${this.personUrl}/login`);
    // this.http.get('...').map(res => <Product[]>res.json());
    return this.http.post<Person>(`${this.personUrl}/login`, { email: email }, this.httpOptions);
    // return this.http.post<Person>(`${this.personUrl}/login`, {firstname: "Aeon", lastname: "Flux", email: "aeonflux@gmail.com"}, this.httpOptions)
  }

  public set value(v: string) {
    this.email = v;
  }

  get value(): string {
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

  getAllContact(): Observable<Contact[]> {
    return this.http.get<Contact[]>(this.contactUrl);
  }

  addContact(contactDetails: Contact): Observable<Contact> {
    return this.http.post<Contact>(this.contactUrl, contactDetails, this.httpOptions);
  }
}