import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AccountinfoComponent } from './accountinfo/accountinfo.component';
import { DashboardComponent } from './accountinfo/dashboard/dashboard.component';

const routes: Routes = [
  {path: 'dashboard', component: DashboardComponent},
  {path: 'accountinfo', component: AccountinfoComponent}
  ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
