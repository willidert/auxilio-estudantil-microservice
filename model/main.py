import json
import pika, sys, os
import numpy as np

from model import Model
from database import Database


def main():
    # try:
    # credentials = pika.PlainCredentials(username='admin', password='admin')
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
    connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@rabbitmq:5672'))
        # channel = connection.channel()
    # except Exception as err:
        # print(err)
    channel = connection.channel()

    channel.queue_declare(queue='model')

    def callback(ch, method, properties, body):
        db = Database()
        model = Model()
        print(" [x] Received %r" % body)
        data = json.loads(body)
        data = data["data"].split()
        email = data[-1]
        data = [int(i) for i in data[:-1]]
        res = model.make_prediction(np.array(data).reshape(1, -1))
        db.update(email, int(res))

    channel.basic_consume(queue='model', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
        print("hue")
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
