import { Component, Input } from '@angular/core';
import { Address } from '../person';

@Component({
  selector: 'app-address',
  templateUrl: './address.component.html',
  styleUrls: ['./address.component.css']
})
export class AddressComponent {
  @Input() addressList: Address[] = [];
  @Input() a = {} as Address

  ngOninit() {
    console.log("contact ", this.a);
  }
}
