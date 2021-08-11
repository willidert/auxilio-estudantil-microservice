import json
import sys
import pika
import numpy as np

from model import Model
from database import Database


def main():
    parameters = pika.URLParameters('amqp://admin:admin@rabbitmq:5672')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='model')

    def callback(body):
        db = Database()
        model = Model()
        print(" [x] Received %r" % body)
        data = json.loads(body)
        data = data["data"].split()
        email = data[-1]
        data = [int(i) for i in data[:-1]]
        res = model.make_prediction(np.array(data).reshape(1, -1))
        db.update(email, int(res))

    channel.basic_consume(queue='model',
                          on_message_callback=callback,
                          auto_ack=True
                          )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
