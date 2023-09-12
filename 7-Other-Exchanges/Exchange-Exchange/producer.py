import pika

connection_parameters = pika.ConnectionParameters(host='localhost', port=5672)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# 声明一个名为 'firstexchange' 的直连交换机，并指定交换机类型为 'direct'
channel.exchange_declare(exchange='firstexchange', exchange_type='direct')

# 声明一个名为 'secondexchange' 的扇出交换机，并指定交换机类型为 'fanout'
channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')

# 将 'secondexchange' 扇出交换机绑定到 'firstexchange' 直连交换机上
channel.exchange_bind(destination='secondexchange', source='firstexchange')

message = "This message has gone through multiple exchanges"

# 使用 'firstexchange' 直连交换机发送消息，路由键为空
channel.basic_publish(exchange='firstexchange', routing_key='', body=message)

print(f"sent message: {message}")

connection.close()
