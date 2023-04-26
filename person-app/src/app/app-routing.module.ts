import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PersonDetailComponent } from './person-detail/person-detail.component';
import { PersonListComponent } from './person-list/person-list.component';
import { LoginComponent } from './login/login.component';
import { AuthGuard } from './utility/app.guard';
// import { AuthGuard } from './auth/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/person', pathMatch: 'full' },
  // { path: '', component: LoginComponent , canActivate: [AuthGuard]},
  // { path: '**', redirectTo: '' }
  // { path: 'login', component: LoginComponent },
  { path: 'person', component: PersonListComponent, loadChildren: () => import('./person-list/person-list.module').then(m => m.PersonListModule), canActivate: [AuthGuard]},
  // { path: 'person/:id', component: PersonDetailComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }