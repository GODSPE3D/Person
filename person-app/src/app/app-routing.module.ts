import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PersonDetailComponent } from './person-detail/person-detail.component';
import { PersonListComponent } from './person-list/person-list.component';
import { LoginComponent } from './login/login.component';
import { AuthGuard } from './utility/app.guard';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { AddressListComponent } from './address-list/address-list.component';
// import { AuthGuard } from './auth/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  // { path: 'person', component: LoginComponent, canActivate: [AuthGuard]},
  { path: 'person', component: PersonListComponent},
  // { path: '**', redirectTo: '' }
  // { path: 'login', component: LoginComponent },
  // { path: 'person', component: PersonListComponent, loadChildren: () => import('./person-list/person-list.module').then(m => m.PersonListModule), canActivate: [AuthGuard] },
  // { path: 'person/:id', component: PersonDetailComponent, loadChildren: () => import('./person-detail/person-detail.module').then(m => m.PersonDetailModule), canActivate: [AuthGuard]},
  { path: 'home', component: DashboardComponent },
  { path: 'person/detail/:id', component: PersonDetailComponent },
  { path: 'person/contact', component: ContactListComponent },
  { path: 'person/address', component: AddressListComponent }
  // { path: 'person', component: PersonDetailComponent, canActivate: [AuthGuard]},
  // { path: 'person', component: PersonDetailComponent, loadChildren: () => import('./person-detail/person-detail.module').then(m => m.PersonDetailModule), canActivate: [AuthGuard]},
  // { path: 'person', component: PersonListComponent, children: [
    // {
    //   path: ':id', component: PersonDetailComponent, loadChildren: () => import('./person-detail/person-detail.module').then(m => m.PersonDetailModule), canActivate: [AuthGuard]
    // }
    // { path: 'login', component: LoginComponent }
  // ]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }