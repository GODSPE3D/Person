import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PersonDetailComponent } from './person-detail/person-detail.component';
import { PersonListComponent } from './person-list/person-list.component';
import { LoginComponent } from './login/login.component';
import { AuthGuard } from './utility/app.guard';
// import { AuthGuard } from './auth/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/person', pathMatch: 'full' },
  // { path: 'person', component: LoginComponent, canActivate: [AuthGuard]},
  // { path: 'person', component: PersonListComponent},
  // { path: '**', redirectTo: '' }
  // { path: 'login', component: LoginComponent },
  // { path: 'person', component: PersonListComponent, loadChildren: () => import('./person-list/person-list.module').then(m => m.PersonListModule), canActivate: [AuthGuard] },
  // { path: 'person/:id', component: PersonDetailComponent }
  // { path: 'person/:id', component: PersonDetailComponent, loadChildren: () => import('./person-detail/person-detail.module').then(m => m.PersonDetailModule), canActivate: [AuthGuard]}
  { path: 'person', component: PersonDetailComponent, loadChildren: () => import('./person-detail/person-detail.module').then(m => m.PersonDetailModule), canActivate: [AuthGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }