import pika

def on_message_received(channel, method, properties, body):
    print(f'received new message: {body}')

connection_parameters = pika.ConnectionParameters(host='localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')

channel.queue_declare(queue='letterbox')

channel.queue_bind(exchange='secondexchange', queue='letterbox')

channel.basic_consume(queue='letterbox', on_message_callback=on_message_received,
                       auto_ack=True)

print('Starting Consuming')

channel.start_consuming()
