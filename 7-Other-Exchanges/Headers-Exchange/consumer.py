import pika
from pika.exchange_type import ExchangeType

def on_message_received(channel, method, properties, body):
    print(f'received new message: {body}')

connection_parameters = pika.ConnectionParameters(host='localhost', port=5672)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare('headersexchange', ExchangeType.headers)

channel.queue_declare(queue='letterbox')

# Rabbitmq 通常要求绑定参数的值（v）为字符串类型。
bind_args = {
    'x-match': 'any',  
    # 绑定条件为 any，当消息的头部属性中的任何一个条件匹配时，消息会被路由到"letterbox"队列
    # 还有一个绑定条件为 all，表示只有都满足了才会发送到相关的队列
    'name': 'brian',
    'age': '21'
}

# arguments=bind_args: 这是一个字典，包含了绑定的条件
channel.queue_bind(exchange='headersexchange', queue='letterbox', arguments=bind_args)

channel.basic_consume(queue='letterbox',auto_ack=True, on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()