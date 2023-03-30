import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShareServiceService {
  readonly url = 'http://localhost:8000'

  constructor(private http: HttpClient) { }

    getAccountInfo():Observable<any[]> {
      return this.http.get<any[]>(this.url + '/accountinfo/')
    }

    get_latest_price(val: any){
      return this.http.get(this.url + '/single_info/' + val + '/')
    }
}
