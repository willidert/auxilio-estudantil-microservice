import json
import pika, sys, os

from model import make_prediction
from database import Database


def main():
    try:
        credentials = pika.PlainCredentials(username='admin', password='admin')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    except Exception:
        return 'deu ruim'
    channel = connection.channel()

    channel.queue_declare(queue='model')

    def callback(ch, method, properties, body):
        db = Database()
        print(" [x] Received %r" % body)
        email = 'teste@gmail.com'
        data = json.loads(body)
        res = make_prediction(data["dados"])
        db.update(email, res)

    channel.basic_consume(queue='model', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
