import { Component, OnInit } from '@angular/core';
import { ShareServiceService } from 'src/app/share-service.service';

@Component({
  selector: 'app-show-info',
  templateUrl: './show-info.component.html',
  styleUrls: ['./show-info.component.css']
})
export class ShowInfoComponent  implements OnInit {

    constructor(private service: ShareServiceService ){}

      accountList:any=[];
      accts:any=[];
      logins:any=[];

      ngOnInit(){
        this.refreshList();
      }

      refreshList(){
        this.service.getAccountInfo().subscribe((account:any)=>{
          this.accountList=account
          this.accts.push(account.login);
        })
      }

      get_latest(log: any){
        this.service.get_latest_price(log)
        this.logins = log
        console.log(this.logins)
        }
        
      }
