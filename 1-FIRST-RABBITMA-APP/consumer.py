# 导入 pika 模块，这是一个 RabbitMQ 客户端库
import pika

# 定义一个消息接收回调函数，当有消息到达时会被调用
def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")

# 定义连接参数，连接到本地 RabbitMQ 服务器
connection_parameters = pika.ConnectionParameters('localhost')

# 创建一个阻塞连接对象，使用定义的连接参数
connection = pika.BlockingConnection(connection_parameters)

# 创建一个通道对象，通过连接与 RabbitMQ 服务器通信
channel = connection.channel()

# 声明一个队列，名为 'letterbox'，确保队列存在
channel.queue_declare(queue='letterbox')

# 设置消息消费回调函数，当从 'letterbox' 队列接收到消息时会调用上面定义的 on_message_received 函数
channel.basic_consume(queue='letterbox', auto_ack=True,
    on_message_callback=on_message_received)

# 打印消息消费开始的提示
print("Starting Consuming")

# 启动消费者，开始监听 'letterbox' 队列中的消息，并调用回调函数处理消息
channel.start_consuming()

