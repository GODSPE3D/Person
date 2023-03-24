import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PersonDetailModule } from '../person-detail/person-detail.module';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';
import {MatCheckboxModule} from '@angular/material/checkbox';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    MatDialogModule,
    PersonDetailModule,
    MatButtonModule,
    MatTableModule,
    MatCheckboxModule
  ],
  exports: [
    MatDialogModule,
    MatButtonModule,
    MatTableModule,
    MatCheckboxModule
  ]
})
export class PersonListModule { }
