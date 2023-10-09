import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AddressListComponent } from './address-list/address-list.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PersonDetailComponent } from './person-detail/person-detail.component';
import { PersonListComponent } from './person-list/person-list.component';
import { ProfileComponent } from './profile/profile.component';
// import { AuthGuard } from './auth/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: DashboardComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'person', component: PersonListComponent},
  { path: 'person/detail', component: PersonDetailComponent },
  { path: 'person/contact', component: ContactListComponent },
  { path: 'person/address', component: AddressListComponent }
  // { path: '**', redirectTo: '' }
  // { path: 'login', component: LoginComponent },
  // { path: 'person', component: PersonListComponent, loadChildren: () => import('./person-list/person-list.module').then(m => m.PersonListModule), canActivate: [AuthGuard] },
  // { path: 'person/:id', component: PersonDetailComponent, loadChildren: () => import('./person-detail/person-detail.module').then(m => m.PersonDetailModule), canActivate: [AuthGuard]},
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