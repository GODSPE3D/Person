import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PersonListComponent } from './person-list/person-list.component';

const routes: Routes = [
  { path: '', redirectTo: '/person/', pathMatch: 'full' },
  { path: 'person/', component: PersonListComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }