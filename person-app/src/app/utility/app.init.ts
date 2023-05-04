import { KeycloakService } from "keycloak-angular";

export function initializeKeycloak(keycloak: KeycloakService): () => Promise<boolean> {
    return () =>
        keycloak.init({
            config: {
                url: 'http://localhost:8080',
                realm: 'person',
                clientId: 'myClient'
            },
            initOptions: {
                onLoad: 'login-required',
                flow: 'standard',
            }
        });
}

// async ngOnInit(): void {
//     // Get user's email
//     await this.getUserEmail();
//     // Get user's data by email
//     this.getUserByEmail();
//  }