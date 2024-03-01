export interface Document {
    person_profile_id: number;
    doc_type: string;
    doc_name: string;
    doc_number: string;
    doc_img: string;
}

export interface Contact {
    person_id: number;
    country_code: number;
    region_code: number;
    phone: number;
}

export interface Role {
    id: number;
    role_type: string;
}

export interface Competitions {
    id: number;
    name: string;
    venue: string;
    organizer: string;
    sponsers: string;
    criteria: string;
    prize: string;
    schedule: string;
    start_date: Date;
    end_date: Date;
}

export interface Address {
    person_id: number;
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
    created_at: Date;
    status: string;
    profile_type: PersonProfile[];
    isExpand: boolean;
}

export interface PersonProfile {
    id: number;
    person_id: number;
    document: Document[];
    profile_type: Role;
    competitions: Competitions[];
}

export interface PersonResponse {
    status_code: number;
    message: string;
    url: string;
    timestamp: Date;
    person: Person;
    list: Person[];
}