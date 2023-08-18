import { Component, Input } from '@angular/core';
import { Address } from '../person';

@Component({
  selector: 'app-address-list',
  templateUrl: './address-list.component.html',
  styleUrls: ['./address-list.component.css']
})
export class AddressListComponent {
  @Input() addressList: Address[] = [];
}
