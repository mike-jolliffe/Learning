import { Component, OnInit } from '@angular/core';

@Component({
  selector: '.app-servers',
  // template: `
  //   <app-server></app-server>
  //   <app-server></app-server>`,
  templateUrl: './servers.component.html',
  styleUrls: ['./servers.component.css']
})
export class ServersComponent implements OnInit {
  allowNewServer = false;
  allowNewUser = false;
  serverCreated = false;
  serverCreationStatus = 'No server was created.';
  serverName = 'default_server_name';
  userCreationStatus = 'No user was created.'
  userName = '';
  servers = ['server', 'server 2']

  constructor() {
    setTimeout(() => {
      this.allowNewServer = true;
    }, 2000);
  }

  ngOnInit() {
  }

  onCreateServer() {
    this.serverCreated = true;
    this.servers.push(this.serverName);
    this.serverCreationStatus = 'You created a new server named ' + '"' + this.serverName + '"';
  }

  onUpdateServerName(event: Event) {
    this.serverName = (<HTMLInputElement>event.target).value
  }

  onCreateUser() {
    this.userCreationStatus = 'You created a new user named ' + '"' + this.userName + '"';
  }

}
