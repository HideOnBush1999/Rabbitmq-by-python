import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="mainexchange", exchange_type=ExchangeType.direct)

message = 'This message might expire'

channel.basic_publish(exchange="mainexchange", routing_key="test", body=message)

print(f'send message:{message}')

connection.close()
