import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CommonModule } from '@angular/common';

import { PersonDetailModule } from '../person-detail/person-detail.module';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatSortModule } from '@angular/material/sort';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import { MatSnackBarModule } from '@angular/material/snack-bar';

@NgModule({
  declarations: [],
  imports: [
    NgbModule,
    CommonModule,
    MatDialogModule,
    PersonDetailModule,
    MatButtonModule,
    MatTableModule,
    MatCheckboxModule,
    MatCardModule,
    MatIconModule,
    MatSortModule,
    ButtonModule,
    TableModule,
    Ng2SearchPipeModule,
    MatSnackBarModule
  ],
  exports: [
    NgbModule,
    MatDialogModule,
    MatButtonModule,
    MatTableModule,
    MatCheckboxModule,
    MatCardModule,
    MatIconModule,
    MatSortModule,
    ButtonModule,
    TableModule,
    Ng2SearchPipeModule,
    MatSnackBarModule
  ]
})
export class PersonListModule { }
