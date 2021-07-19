#!/usr/bin/env python
import pika, sys, os
import json
from clean import gloriosafuncao
from send import send

def main():
    connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@rabbitmq:5672'))
    channel = connection.channel()

    channel.queue_declare(queue='form', durable=True)

    def callback(ch, method, properties, body):
        #c = body.decode()
        print(" [x] Received %r" % body.decode())
        c = json.loads(body)
        rc = gloriosafuncao(c)
        rc = ' '.join([str(i) for i in rc[0]])
        data = json.dumps({"data": rc })
        send(data)
        

    channel.basic_consume(queue='form', on_message_callback=callback, auto_ack=True)

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
