import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

chanel_receiver = connection.channel()

chanel_receiver.queue_declare(queue='worker_queue', durable=True)

print("Waiting for messages...")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(8)
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


chanel_receiver.basic_qos(prefetch_count=1)
chanel_receiver.basic_consume(queue='worker_queue', on_message_callback=callback, auto_ack=True)

chanel_receiver.start_consuming()
