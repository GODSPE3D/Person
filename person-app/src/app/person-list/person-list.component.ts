import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { Person, PersonColumns } from '../person';
import { PersonService } from '../person.service';
import { ConfirmationService, MessageService } from 'primeng/api';
import { PersonDetailComponent } from '../person-detail/person-detail.component';
import { SelectionModel } from '@angular/cdk/collections';
import { MatTableDataSource } from '@angular/material/table';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrls: ['./person-list.component.css'],
  providers: [MessageService, ConfirmationService]
})
export class PersonListComponent implements OnInit {
  personDialog!: boolean;
  person: Person[] = [];
  newPerson = {} as Person;
  selectedPeople: Person[] = [];
  currentItem!: Person;
  yes!: true;
  submitted: boolean | undefined;
  status: boolean = false;

  @ViewChild('addP', {static: true}) addP!: TemplateRef<any>;
  @ViewChild(PersonDetailComponent) child!: PersonDetailComponent;

  selection = new SelectionModel<Person>(false, []);

  constructor(private personService: PersonService, public dialog: MatDialog) { }

  @ViewChild('secondDialog', { static: true }) secondDialog!: TemplateRef<any>;
  @ViewChild('this.child.customDialog') print!: TemplateRef<any>;
  
  openDialogWithTemplateRef(templateRef: TemplateRef<any>) {
    this.dialog.open(templateRef);
  }

  buttonClick() {
    this.child.openDialog();
  }

  buttonClick2() {
    this.child.openDialog2();
  }

  openDialogWithoutRef() {
    this.dialog.open(this.secondDialog);
    console.log(this.secondDialog);
  }

  displayedColumns: string[] = PersonColumns.map((col) => col.key);
  dataSource = new MatTableDataSource<Person>();
  columnsSchema: any = PersonColumns;
  valid: any = {}

  ngOnInit(): void {
    this.getPersonAll();
  }

  onPersonToggled(person: Person) {
    this.selection.toggle(person);
    console.log(this.selection.selected);
  }

  // isAnySelected() {
  //   return this.dataSource.((item: any) => item.isSelected);
  // }

  getPersonAll(): void {
    // this.personService.getPersonAll()
    //   .subscribe(person => this.person = person);
    this.personService.getPersonAll().subscribe((res: any) => {
      this.dataSource.data = res;
      console.log(this.dataSource.data);
    })
  }

  editPerson(newP: Person) {
    // this.personService.updatePerson(person._id, person).subscribe(() => person.isEdit = false);
    if (newP._id == null) {
      this.personService.addPerson(newP).subscribe((newPerson: Person) => {
        newP._id = newPerson._id;
        newP.isEdit = false;
      });
    } else {
      this.personService.updatePerson(newP._id, newP).subscribe(() => newP.isEdit = false);
    }
  }

  addPerson() {
    const newRow: Person = {
      firstname: '',
      lastname: '',
      email: '',
      contact: 0,
      address: '',
      education: '',
      pwd: '',
      aadhaar: 0,
      isEdit: true,
      isSelected: false,
    };
    this.personService.addPerson(newRow);
  }

  onRowClicked(row: number) {
    console.log('Row clicked: ', row);
  }

  inputHandler(e: any, id: number, key: string) {
    if (!this.valid[id]) {
      this.valid[id] = {}
    }
    this.valid[id][key] = e.target.validity.valid
  }

  disableSubmit(id: number) {
    if (this.valid[id]) {
      return Object.values(this.valid[id]).some((item) => item === false)
    }
    return false
  }

  isAllSelected() {
    return this.dataSource.data.every((item) => item.isSelected)
  }

  isAnySelected() {
    return this.dataSource.data.some((item) => item.isSelected)
  }

  selectAll(event: any) {
    this.dataSource.data = this.dataSource.data.map((item) => ({
      ...item,
      isSelected: event.checked,
    }))
  }

  // openNew() {
  //   this.newPerson;
  //   this.submitted = false;
  //   this.personDialog = true;
  // }

  // showchildModal() {
  //   this.personService.childModal = true;
  // }

  // callChild() {
  //   this.child.showModalDialog();
  // }

  // deleteSelectedPerson() {
  //   this.confirmationService.confirm({
  //     message: 'Are you sure you want to delete the selected people?',
  //     header: 'Confirm',
  //     icon: 'pi pi-exclamation-triangle',
  //     accept: () => {
  //       this.person = this.person.filter(val => !this.selectedPeople.includes(val));
  //       this.selectedPeople = null as any;
  //       this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'Products Deleted', life: 3000 });
  //     }
  //   })
  // }

  // goBack(): void {
  //   this.location.back();
  // }

  // save(): void {
  //   if (this.newPerson) {
  //     this.personService.updatePerson(this.newPerson).subscribe(() => this.goBack());
  //   }
  // }

  // editPerson(editPerson: Person) {
  //   this.newPerson = { ...editPerson };
  //   this.personDialog = true;
  // }

  // deletePerson(delPerson: Person) {
  //   this.confirmationService.confirm({
  //     message: 'Are you sure you want to delete ' + delPerson.firstname + '?',
  //     header: 'Confirm',
  //     icon: 'pi pi-exclamation-triangle',
  //     accept: () => {
  //       // this.delete(delPerson);
  //       // this.person = this.person.filter(val => val._id !== delPerson._id);
  //       // this.selectedPeople = null as any;
  //       // this.personService.deletePerson(delPerson._id).subscribe();
  //       this.person = this.person.filter(p => p !== delPerson);
  //       this.personService.deletePerson(delPerson._id).subscribe();
  //       this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'Products Deleted', life: 3000 });
  //     }
  //   })
  // }

  // addName(newName: string) {
  //   this.newPerson.firstname = newName;
  //   console.log(this.newPerson.firstname);
  //   this.person.push(this.newPerson);
  //   console.log(this.person);
  //   // this.personService.addPerson(this.newPerson).subscribe();
  // }

  // hideDialog() {
  //   this.personDialog = false;
  //   this.submitted = false;
  // }

  // saveProduct() {
  //   this.submitted = true;

  //   if (this.newPerson.firstname.trim()) {
  //     if (this.newPerson._id) {
  //       this.person[(this.newPerson._id)] = this.newPerson;
  //       this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'Product Updated', life: 3000 });
  //     }
  //     else {
  //       // this.personService.updatePerson(this.newPerson).subscribe(() => this.goBack())
  //       this.person.push(this.newPerson);
  //       this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'Product Created', life: 3000 });
  //     }

  //     // this.[this.person] = [...this.person];
  //     this.personDialog = false;
  //     // this.newPerson = {};
  //   }
  // }

  selectPerson(x: Person) {
    this.currentItem = x;
  }

  deletePerson(id: number) {
    // this.person = this.person.filter(p => p !== newP);
    // this.personService.deletePerson(newP._id).subscribe();
    this.personService.deletePerson(id).subscribe(() => {
      this.dataSource.data = this.dataSource.data.filter(
        (p: Person) => p._id !== id
      );
    });
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
