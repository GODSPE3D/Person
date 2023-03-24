import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PersonDetailComponent } from './person-detail/person-detail.component';
import { PersonListComponent } from './person-list/person-list.component';

const routes: Routes = [
  { path: '', redirectTo: '/person', pathMatch: 'full' },
  { path: 'person', component: PersonListComponent },
  { path: 'person/:id', component: PersonDetailComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }