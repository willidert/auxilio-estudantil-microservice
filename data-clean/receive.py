#!/usr/bin/env python
import pika, sys, os
import json
from clean import gloriosafuncao
from send import send

def main():
    credentials = pika.PlainCredentials(username='admin', password='admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='form', durable=True)

    def callback(ch, method, properties, body):
        #c = body.decode()
        print(" [x] Received %r" % body.decode())
        c = json.loads(body)
        rc = gloriosafuncao(c)
        data = json.dumps({"data":rc})
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