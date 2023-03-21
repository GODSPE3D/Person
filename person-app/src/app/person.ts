const _id = '_id' as string;

export interface IPerson {
    _id: number;
    firstname: string;
    lastname: string;
    email: string;
    contact: number;
    address: string;
    education: string;
    pwd: string;
    aadhaar: number;

    // constructor(
    //     public _id: number,
    //     public firstname: string,
    //     public lastname: string,
    //     public email: string,
    //     public contact: number,
    //     public address: string,
    //     public education: string,
    //     public pwd: string,
    //     public aadhaar: number
    // ) { }
}