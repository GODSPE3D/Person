export interface Person {
    _id: number;
    firstname: string;
    lastname: string;
    email: string;
    contact: number;
    address: string;
    education: string;
    password: string;
    aadhaar: number;
}

export type P = keyof Person;

export const PersonColumns = [
    // {
    //     key: 'isSelected',
    //     type: 'isSelected',
    //     label: '',
    // },
    {
        key: 'firstname',
        type: 'text',
        label: 'First Name',
    },
    {
        key: 'lastname',
        type: 'text',
        label: 'Last Name',
    },
    {
        key: 'email',
        type: 'email',
        label: 'Email',
        required: true,
    },
    {
        key: 'contact',
        type: 'number',
        label: 'Contact',
    },
    {
        key: 'address',
        type: 'text',
        label: 'Address',
    },
    {
        key: 'education',
        type: 'text',
        label: 'Education',
    },
    // {
    //     key: 'isEdit',
    //     type: 'isEdit',
    //     label: '',
    // },
];