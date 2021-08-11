#!/usr/bin/env python
import pika


def send(data):
    connection = pika.BlockingConnection(
        pika.URLParameters('amqp://admin:admin@rabbitmq:5672'))
    channel = connection.channel()

    channel.queue_declare(queue='model')

    channel.basic_publish(exchange='', routing_key='model', body=data)
    print(" [x] Sent 'Hello World!'")
    connection.close()
