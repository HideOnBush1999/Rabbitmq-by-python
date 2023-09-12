import pika
import uuid

def on_reply_message_received(channel, method, properties, body):
    print(f"reply recieved: {body}")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# 声明一个队列，用于接收回复消息
reply_queue = channel.queue_declare(queue='', exclusive=True)  # 自动给队列分配个名字

# 接收回复
channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, 
                    on_message_callback=on_reply_message_received)

# 声明一个队列，用于发送请求消息
channel.queue_declare(queue='request-queue')

# 作为请求的唯一标识符，以便在接收响应时能够将其与请求关联起来
cor_id = str(uuid.uuid4())
print(f"Sending Request: {cor_id}")

# 用于设置消息的属性
# reply_to 指定了客户端期望接收响应的队列  correlation_id 用于标识请求和相应之间的关联关系
props = pika.BasicProperties(reply_to=reply_queue.method.queue, correlation_id=cor_id)

# 发送响应
channel.basic_publish(exchange='', routing_key='request-queue', properties=props,
                    body='Can I request a reply?')

print("Starting Client")

channel.start_consuming()

