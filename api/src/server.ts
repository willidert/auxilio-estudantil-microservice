import express from 'express';
import { Application } from 'express';
import { router } from './routes/routes';
import cors from 'cors';
import * as database from './database';
import rabbitmq from './RabbitMQ/rabbitmq-server';

export class SetupServer {
  private app: Application = express();

  constructor(private port = 3333) {}

  public async init() {
    this.setupExpress();
    await this.databaseSetup();
    await rabbitmq.start();
  }

  private setupExpress() {
    this.app.use(express.json());
    this.app.use(
      cors({
        origin: '*',
      })
    );
    this.app.use(router);
  }

  public getApp(): Application {
    return this.app;
  }

  public start(): void {
    this.app.listen(this.port, () => {
      console.log(`Server listening of port: ${this.port}`);
    });
  }

  private async databaseSetup(): Promise<void> {
    await database.connect();
  }

  public async close(): Promise<void> {
    await database.close();
  }
}
