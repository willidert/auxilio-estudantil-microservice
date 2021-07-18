import { Connection, Channel, connect, Message } from 'amqplib';

class RabbitMQServer {
  private conn!: Connection;
  private channel!: Channel;

  constructor(private uri: string) {}

  async start(): Promise<void> {
    this.conn = await connect(this.uri);
    this.channel = await this.conn.createChannel();
  }

  async publishInQueue(queue: string, message: string) {
    this.channel.assertQueue(queue);
    this.channel.sendToQueue(queue, Buffer.from(message));
  }

  async consume(queue: string, callback: (message: Message) => void) {
    return this.channel.consume(queue, (message) => {
      callback(message);
      console.log(message?.content.toString());
      this.channel.ack(message);
    });
  }
}

export default new RabbitMQServer('amqp://admin:admin@rabbitmq:5672');
