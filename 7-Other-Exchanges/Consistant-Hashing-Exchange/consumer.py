import pika

def queue_1_on_message_received(channel, method, properties, body):
    print(f'queue 1 received new message: {body}')

def queue_2_on_message_received(channel, method, properties, body):
    print(f'queue 2 received new message: {body}')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='samplehashing', exchange_type='x-consistent-hash')

channel.queue_declare(queue='queue_1')

channel.queue_declare(queue='queue_2')

# 将 queue_1 和 samplehashing 进行绑定，并设定权重为 1
channel.queue_bind(exchange='samplehashing', queue='queue_1', routing_key='1')

# 将 queue_2 和 samplehashing 进行绑定，并设定权重为 1
channel.queue_bind(exchange='samplehashing', queue='queue_2', routing_key='1')

channel.basic_consume(queue='queue_1', on_message_callback=queue_1_on_message_received, auto_ack=True)

channel.basic_consume(queue='queue_2', on_message_callback=queue_2_on_message_received, auto_ack=True)

print('Starting Consuming')

channel.start_consuming()