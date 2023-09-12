import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host="localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# 声明了名为"pubsub"的交换器，并将其类型设置为"fanout"。
# 如果交换器在之前已经被声明，再次声明它不会导致错误或其他不良影响，但也不会有任何实际的效果。
channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

message = "Hello I want to broadcast this message to all the subscribers"

channel.basic_publish(exchange="pubsub", routing_key="", body=message)

print(f"sent message: {message}")

connection.close()
