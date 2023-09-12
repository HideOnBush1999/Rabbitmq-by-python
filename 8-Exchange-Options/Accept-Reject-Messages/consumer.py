import pika
from pika.exchange_type import ExchangeType

# 当接收到消息时触发的回调函数
def on_message_received(ch, method, properties, body):
    
    if (method.delivery_tag % 5 == 0):
        #  ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)

        # 拒绝消息（不重新入队），并确认多个消息 可以一次性拒绝多个消息
         ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False, multiple=True)
        # requeue 参数为 True，则拒绝的消息将被重新放入队列中，等待后续再次投递 只能处理单个消息 
        # ch.basic_reject(delivery_tag=method.delivery_tag, requeue=True)
    else:
        print(f'Received new message: {method.delivery_tag}')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='accept_reject_exchange', exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='letterbox')
channel.queue_bind('letterbox', 'accept_reject_exchange')

channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()
