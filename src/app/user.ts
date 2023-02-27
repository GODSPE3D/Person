export class User {
    constructor(
        public id: number,
        public firstname: string,
        public lastname: string,
        public email: string,
        public contact: number,
        public address: string,
        public education: string,
        public pwd: string,
        public aadhaar: number
    ) { }
    // id?: number;
    // firstname: string;
    // email: string;
    // pwd: string;
}