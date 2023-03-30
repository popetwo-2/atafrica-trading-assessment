import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts';
import { ShareServiceService } from 'src/app/share-service.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  

  constructor(private service: ShareServiceService ){}

  Highcharts: typeof Highcharts = Highcharts;
  chartOptions: any;
  date: any[] = []
  equity: any[] = [];
  balance: any[] = [];
  login: any[] = [];
  ngOnInit(){
    this.getAccountInfo();
  }

  getAccountInfo(){
    this.service.getAccountInfo().subscribe((account:any) =>{
      account.forEach((data:any) => {
        this.equity.push(data.equity)
        this.balance.push(data.balance)
        this.date.push(data.date)
        this.login.push(data.login)
    })
    this.chartOptions = {
      xAxis: {
        name: 'Date',
        categories: this.date
      },
      series: [{
        name: 'Balance',
        data: this.balance,
      },
      {
        name: 'Equity',
        data: this.equity,
      }, ],
      chart: {
        type: "bar",
      },
  }
  
    
  });
}
}

