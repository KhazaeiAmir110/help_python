import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

chanel = connection.channel()

chanel.queue_declare(queue='hello')

chanel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

connection.close()
