import config from 'config';
import { SetupServer } from './server';

(async () => {
  const server = new SetupServer(config.get('App.port'));
  await server.init();
  server.start();
})();
