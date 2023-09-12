import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# 声明交换机的名称为 routing，交换机的类型为 direct
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

message = 'This message needs to be routed'

# 将一条消息发布到一个名为"routing"的直连交换器中，并指定消息的路由键。
# channel.basic_publish(exchange='routing', routing_key='both', body=message)   # 这行代码与下面两行代码一样

channel.basic_publish(exchange='routing', routing_key='paymentsonly', body=message)
channel.basic_publish(exchange='routing', routing_key='analyticsonly', body=message)

print(f'sent message: {message}')

connection.close()
