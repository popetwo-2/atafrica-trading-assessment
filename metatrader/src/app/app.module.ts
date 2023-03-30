import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AccountinfoComponent } from './accountinfo/accountinfo.component';
import { DashboardComponent } from './accountinfo/dashboard/dashboard.component';
import {ShareServiceService} from './share-service.service';
import {HttpClientModule} from '@angular/common/http';
import { ShowInfoComponent } from './accountinfo/show-info/show-info.component';
import { HighchartsChartModule } from 'highcharts-angular';

@NgModule({
  declarations: [
    AppComponent,
    AccountinfoComponent,
    DashboardComponent,
    ShowInfoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CommonModule,
    HighchartsChartModule,
  ],
  providers: [ShareServiceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
