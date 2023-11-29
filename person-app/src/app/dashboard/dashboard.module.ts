import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

// import {MatTabsModule} from '@angular/material/tabs';
import { NgbCollapseModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    NgbCollapseModule
    // MatTabsModule
  ],
  exports: [
    // MatTabsModule
  ]
})
export class DashboardModule { }
