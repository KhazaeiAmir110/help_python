import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

chanel_receiver = connection.channel()

chanel_receiver.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


chanel_receiver.basic_consume(queue='hello',on_message_callback=callback, auto_ack=True)

chanel_receiver.start_consuming()
