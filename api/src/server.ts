import express from 'express';
import { Application } from 'express';
import { router } from './routes/routes';
import cors from 'cors';

export class SetupServer {
  private app: Application = express();

  constructor(private port = 3333) {}

  public init() {
    this.setupExpress();
  }

  private setupExpress() {
    this.app.use(express.json());
    this.app.use(router);
    this.app.use(
      cors({
        origin: '*',
      })
    );
  }

  public getApp(): Application {
    return this.app;
  }

  public start(): void {
    this.app.listen(this.port, () => {
      console.log(`Server listening of port: ${this.port}`);
    });
  }
}
