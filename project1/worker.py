import time

import pika

connection_project1 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

chanel_receiver = connection_project1.channel()

chanel_receiver.queue_declare(queue='project1_chanel1_queue1', durable=True)
chanel_receiver.queue_declare(queue='project1_chanel2_queue2', durable=True)
chanel_receiver.queue_declare(queue='project1_chanel2_queue1', durable=True)

print("Waiting for messages...")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("channel_number: %d" % ch)
    print("routing_key: %s" % method.routing_key)
    time.sleep(4)
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


chanel_receiver.basic_qos(prefetch_count=1)

chanel_receiver.basic_consume(queue='project1_chanel1_queue1', on_message_callback=callback)
chanel_receiver.basic_consume(queue='project1_chanel2_queue1', on_message_callback=callback)
chanel_receiver.basic_consume(queue='project1_chanel2_queue1', on_message_callback=callback)
chanel_receiver.basic_consume(queue='project1_chanel3_queue3', on_message_callback=callback)

chanel_receiver.start_consuming()

print("Finished")
