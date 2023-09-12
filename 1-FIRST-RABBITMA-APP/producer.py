# 导入 pika 模块，这是一个 RabbitMQ 客户端库
import pika

# 定义连接参数，连接到本地 RabbitMQ 服务器
connection_parameters = pika.ConnectionParameters('localhost')

# 创建一个连接对象，使用定义的连接参数
connection = pika.BlockingConnection(connection_parameters)

# 创建一个通道对象，通过连接与 RabbitMQ 服务器通信
channel = connection.channel()

# 声明一个队列，名为 'letterbox'，确保队列存在
channel.queue_declare(queue='letterbox')

# 准备要发送的消息内容
message = "Hello this is my first message"

# 使用通道发送消息，将消息发布到 'letterbox' 队列
channel.basic_publish(exchange='', routing_key='letterbox', body=message)

# 打印发送的消息内容
print(f"sent message: {message}")

# 关闭连接，释放资源
connection.close()
