import { Pipe, PipeTransform } from '@angular/core';
import { Person } from './person';

@Pipe({
  name: 'search'
})
export class SearchPipe implements PipeTransform {

  transform(value: any, args?: any): any {
    if (!value) return null;
    if (!args) return value;

    args = args.toLowerCase();

    return value.filter((val: any) => {
      let rVal = (val.firstname.toLowerCase().includes(args)) || (val.lastname.toLowerCase().includes(args)) || (val.email.toLowerCase().includes(args));
      return rVal;
    })
  }
}
