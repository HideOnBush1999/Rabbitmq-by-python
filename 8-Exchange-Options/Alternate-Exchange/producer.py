import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='altexchange', exchange_type=ExchangeType.fanout)

channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct,
                        arguments={'alternate-exchange': 'altexchange'})

message = 'Hello this is my first message'

# mainexchange 没有绑定过 test 这个路由键的队列，所以没有队列可以接收来自 mainexchange 的消息
channel.basic_publish(exchange='mainexchange', routing_key='test', body=message)

print(f"sent message:{message}")

connection.close()

