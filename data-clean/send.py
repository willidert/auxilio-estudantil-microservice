#!/usr/bin/env python
import pika

def send(data):
    credentials = pika.PlainCredentials(username='admin', password='admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='model')

    channel.basic_publish(exchange='', routing_key='model', body=data)
    print(" [x] Sent 'Hello World!'")
    connection.close()