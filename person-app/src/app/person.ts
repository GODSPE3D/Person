export interface Contact {
    country_code: number;
    region_code: number;
    phone: number;
}

export interface Address {
    address_type: string;
    flat_no: string;
    area: string;
    locality: string;
    city: string;
    state: string;
    country: string;
    pin: string;
}

export interface Person {
    id: number;
    firstname: string;
    lastname: string;
    email: string;
    contact: Contact[];
    address: Address[];
    education: string;
    password: string;
    aadhaar: number;
}

// const person = {} as Person;