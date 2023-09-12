import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# 选用 headers 类型的交换机
channel.exchange_declare('headersexchange', ExchangeType.headers)

message = 'This message will be sent with headers'

# 将一条包含指定消息内容和头部属性的消息发布到名为"headersexchange"的头部交换器
channel.basic_publish(exchange='headersexchange',
    routing_key='',   # 消息的路由是基于消息属性头进行匹配的，而不是路由键，所以为空字符串
    body=message,
    properties=pika.BasicProperties(headers={'name': 'brian'}) 
    # BasicProperties 用于设置消息属性的参数
    # headers 表示消息的头部属性，可以包含任何自定义的键值对
)

print(f'sent message:{message}')

connection.close()
