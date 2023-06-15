import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpResponse,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { KeycloakService } from 'keycloak-angular';

@Injectable()
export class ExampleInterceptorInterceptor implements HttpInterceptor {

  constructor(private kcService: KeycloakService) {}

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const authToken = this.kcService.getKeycloakInstance().token || '';
    // return next.handle(request);
    request = request.clone({
      setHeaders: {
        'Authorization': 'Bearer' + authToken
      }
    });

    console.log('Authorization interceptor' + authToken);
    
    return next.handle(request);
  }
}
