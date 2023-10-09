import { APP_INITIALIZER, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { PersonService } from './person.service';
import { PersonListModule } from './person-list/person-list.module';
import { PersonDetailModule } from './person-detail/person-detail.module';
import { PersonListComponent } from './person-list/person-list.component';
import { PersonDetailComponent } from './person-detail/person-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './login/login.component';
import { KeycloakAngularModule, KeycloakBearerInterceptor, KeycloakService } from 'keycloak-angular';
import { initializeKeycloak } from './utility/app.init';
import { ExampleInterceptorInterceptor } from './example-interceptor.interceptor';
import { DashboardComponent } from './dashboard/dashboard.component';
import { DashboardModule } from './dashboard/dashboard.module';
import { AddressComponent } from './address/address.component';
import { ContactComponent } from './contact/contact.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { AddressListComponent } from './address-list/address-list.component';
import { SearchPipe } from './search.pipe';
import { ProfileComponent } from './profile/profile.component';
// import { MatDialogModule } from '@angular/material/dialog';
// import { MatButtonModule } from '@angular/material/button';
// import { MatIconModule } from '@angular/material/icon';
// import { MatFormFieldModule } from '@angular/material/form-field';

@NgModule({
  declarations: [
    AppComponent,
    PersonListComponent,
    PersonDetailComponent,
    LoginComponent,
    DashboardComponent,
    AddressComponent,
    ContactComponent,
    ContactListComponent,
    AddressListComponent,
    SearchPipe,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    // MatDialogModule,
    PersonListModule,
    PersonDetailModule,
    BrowserAnimationsModule,
    KeycloakAngularModule,
    DashboardModule
    // MatButtonModule,
    // MatIconModule,
    // MatFormFieldModule
  ],
  providers: [PersonService, 
    {
      provide: HTTP_INTERCEPTORS,
      useClass: KeycloakBearerInterceptor,
      multi: true
    }, 
    {
      provide: APP_INITIALIZER,
      useFactory: initializeKeycloak,
      multi: true,
      deps: [KeycloakService]
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
