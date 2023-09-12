import pika

# 回调函数中服务器打印请求消息的相关信息，发送响应消息到指定的回复队列
def on_request_message_received(ch, method, properties, body):
    print(f"Received Request: {properties.correlation_id}")
    ch.basic_publish('', routing_key=properties.reply_to,
                    body=f'Hey its your reply to {properties.correlation_id}')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='request-queue')

# 设置了一个消费者监听 "request-queue" 队列。当有请求消息到达队列时，执行回调函数
channel.basic_consume(queue='request-queue', auto_ack=True,
                    on_message_callback=on_request_message_received)

print("Starting Server")

channel.start_consuming()
