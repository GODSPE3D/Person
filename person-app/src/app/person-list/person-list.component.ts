import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';

import { Person } from '../person';
import { PersonService } from '../person.service';
import { ConfirmationService, MessageService } from 'primeng/api';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable, switchMap } from 'rxjs';
import { Location } from '@angular/common';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrls: ['./person-list.component.css'],
  styles: [`
      :host ::ng-deep .p-dialog .product-image {
          width: 150px;
          margin: 0 auto 2rem auto;
          display: block;
      }
  `],
  providers: [MessageService, ConfirmationService]
})
export class PersonListComponent implements OnInit {
  person: Person[] = [];
  currentItem: Person | undefined;

  constructor(private personService: PersonService) { }

  ngOnInit(): void {
    this.getPerson();
  }

  getPerson(): void {
    this.personService.getPerson().subscribe(person => this.person = person);
  }

  selectPerson(x: Person) {
    this.currentItem = x;
  }

  delete(newP: Person): void {
    this.person = this.person.filter(p => p !== newP);
    this.personService.deletePerson(newP._id).subscribe();
  }

  // selectPerson(newP: Person) { this.selectedPerson = newP; }

  // gotoPer(hero: Person) {
  //   const heroId = hero ? hero._id : null;
  //   this.router.navigate(['/person', {id: heroId}]);
  // }

  // getPer() {
  //   const id = parseInt(this.route.snapshot.paramMap.get('id')!);
  // const id = this.route.snapshot.paramMap.get(":id");
  // console.log(id);
  // this.personService.getPer(id).subscribe((user: Person) => {
  //   this.p = user;
  //   return this.p;
  //   console.log(this.p);
  // });

  // this.hero$ = this.route.paramMap.pipe(
  //   switchMap(params => {
  //     this.selectedId = Number(params.get('id'));
  //     return this.personService.getPer(this.selectedId);
  //   })
  // )
  // const id = + this.route.snapshot.paramMap.get('id');
  // var x = <HTMLAnchorElement>document.querySelector('#detail');
  // this.personService.getPer(x).subscribe(user => this.p = user);
  // this.personService.getPer(id).subscribe(user => this.p = user);
  // this.personService.getPer().params.subscribe((pa: Person) => {
  //   const id = +pa['_id'];
  //   console.log(id);
  // })
  // this.route.paramMap.subscribe(params => {
  //   this.p = params.get("firstname");
  // })
  // this.p = this.route.snapshot.paramMap.get("id");
  // }

  // goBack(): void {
  //   this.location.back();
  // }

  // getValue() {
  //   console.log(this.detail.nativeElement.value);
  // }

  // addPerson(singlePerson: Person) {
  //   this.personService.addPerson(singlePerson).subscribe(p => this.person.push(p));
  // }

  // hideDialog() {
  //     this.personDialog = false;
  //     this.submitted = false;
  // }

  //   saveProduct() {
  //     this.submitted = true;

  //     if (this.p.firstname.trim()) {
  //         if (this.p._id) {
  //             this.p[this.findIndexById(this.product.id)] = this.product;
  //             this.messageService.add({severity:'success', summary: 'Successful', detail: 'Product Updated', life: 3000});
  //         }
  //         else {
  //             this.product.id = this.createId();
  //             this.product.image = 'product-placeholder.svg';
  //             this.products.push(this.product);
  //             this.messageService.add({severity:'success', summary: 'Successful', detail: 'Product Created', life: 3000});
  //         }

  //         this.products = [...this.products];
  //         this.productDialog = false;
  //         this.product = {};
  //     }
  // }

  // add(name: string): void {
  //   name = name.trim()
  // }

  // editPerson() {

  // }

  // getUserName(id: number) {
  //   this.personService.GetUser(id).pipe(map(response => {
  //     this.person = response;
  //   }))
  // }
}
