import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# 声明了一个名为 samplehashing, 类型为 x-consistent-hash 的交换机
channel.exchange_declare(exchange='samplehashing', exchange_type='x-consistent-hash')

message = 'Hello hash the routing key and pass me on please!'

routing_key_to_hash = 'hash me'

# routing_key_to_hash 字符串进行 hash，会根据这个 hash 值来决定将这条消息发送到那条队列中
channel.basic_publish(exchange='samplehashing', routing_key=routing_key_to_hash, body=message)

print(f'sent message: {message}')

connection.close()