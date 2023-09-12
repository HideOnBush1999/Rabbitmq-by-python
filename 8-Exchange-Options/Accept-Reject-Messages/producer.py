import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='accept_reject_exchange', exchange_type=ExchangeType.fanout)

message = 'Lets send this'

while True:
    channel.basic_publish(exchange='accept_reject_exchange', routing_key='', body=message)
    print("Sent message: {}".format(message))
    input('Press any key to continue')
