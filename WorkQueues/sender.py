import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

chanel = connection.channel()

chanel.queue_declare(queue='worker_queue', durable=True)

message = "THis is a First Massage"

chanel.basic_publish(exchange='', routing_key='worker_queue', body=message)

connection.close()
