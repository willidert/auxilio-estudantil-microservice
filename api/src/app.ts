import { SetupServer } from './server';

const server = new SetupServer();
server.init(); // initialize async services
server.start();
