import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { MatTableModule } from '@angular/material/table';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { DialogModule } from 'primeng/dialog';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatListModule,
    FormsModule,
    ReactiveFormsModule,
    DialogModule,
    ButtonModule,
    TableModule,
    MatTableModule,
    MatSnackBarModule
  ],
  exports: [
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatListModule,
    FormsModule,
    ReactiveFormsModule,
    DialogModule,
    ButtonModule,
    TableModule,
    MatTableModule,
    MatSnackBarModule
  ]
})
export class PersonDetailModule { }
