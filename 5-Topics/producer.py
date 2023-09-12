import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host='localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='topic', exchange_type=ExchangeType.topic)

user_payments_message = 'A europan user paid for something'

channel.basic_publish(exchange='topic', routing_key='user.europe.payments', body=user_payments_message)

print(f'sent message: {user_payments_message}')

business_order_message = 'A european business ordered goods'

channel.basic_publish(exchange='topic', routing_key='business.europe.orders', body=business_order_message)

print(f'sent message: {business_order_message}')

connection.close()
