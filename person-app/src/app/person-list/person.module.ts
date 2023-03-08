import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { TableModule } from 'primeng/table';
import { ButtonModule } from 'primeng/button';
import { DialogModule } from 'primeng/dialog';
import { AccordionModule } from 'primeng/accordion';
import { PanelModule } from 'primeng/panel';
import { PanelMenuModule } from 'primeng/panelmenu';
import { RadioButtonModule } from 'primeng/radiobutton';

import { PersonListComponent } from './person-list.component';



@NgModule({
  declarations: [
    PersonListComponent
  ],
  imports: [
    FormsModule,
    CommonModule,
    HttpClientModule,
    TableModule,
    AccordionModule,
    PanelModule,
    ButtonModule,
    RadioButtonModule,
    DialogModule,
    BrowserAnimationsModule,
    PanelMenuModule
  ],
  exports: [
    PersonListComponent
  ]
})
export class PersonModule { }