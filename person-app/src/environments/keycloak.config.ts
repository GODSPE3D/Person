// import { KeycloakConfig } from "keycloak-js";

// export const keycloakConfig: KeycloakConfig = {
//     url: 'http://localhost:8080',
//     realm: 'personRealm',
//     clientId: 'myClient',
// };

import { KeycloakConfig } from 'keycloak-js';

const keycloakConfig: KeycloakConfig = {
    url: 'http://localhost:8080',
    realm: 'personRealm',
    clientId: 'myClient',
};

export default keycloakConfig;

// "admin" for managing Keycloak = http://localhost:8080/
// "myuser" to login which is same as person login = http://localhost:8080/realms/personRealm/account