import pika
from pika.exchange_type import ExchangeType

def alt_queue_on_received(ch, method, properties, body):
    print(f'Alt - received new message: {body}')

def main_queue_on_received(ch, method, properties, body):
    print(f'Main - received new message: {body}')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='altexchange', exchange_type=ExchangeType.fanout)

channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct, 
                        arguments={'alternate-exchange': 'altexchange'})

channel.queue_declare(queue='alt_queue')
channel.queue_bind(exchange='altexchange', queue='alt_queue')

channel.basic_consume(queue='alt_queue', on_message_callback=alt_queue_on_received)

channel.queue_declare(queue='main_queue')
channel.queue_bind(exchange='mainexchange', queue='main_queue')

channel.basic_consume(queue='main_queue', on_message_callback=main_queue_on_received)

print('Starting Consuming')

channel.start_consuming()

