import pika

connection_project1 = pika.BlockingConnection(pika.ConnectionParameters())

chanel1 = connection_project1.channel(channel_number=1)
chanel2 = connection_project1.channel(channel_number=2)
chanel3 = connection_project1.channel(channel_number=3)

chanel1.queue_declare(queue='project1_chanel1_queue1', durable=True)
chanel1.queue_declare(queue='project1_chanel2_queue2', durable=True)

chanel2.queue_declare(queue='project1_chanel2_queue1', durable=True)

chanel3.queue_declare(queue='project1_chanel3_queue1', durable=True)
chanel3.queue_declare(queue='project1_chanel3_queue2', durable=True)
chanel3.queue_declare(queue='project1_chanel3_queue3', durable=True)

chanel1.basic_publish(exchange='', routing_key="project1_chanel1_queue1", body="THis is a First Massage")
chanel1.basic_publish(exchange='', routing_key="project1_chanel1_queue1", body="THis is a First2 Massage")
chanel1.basic_publish(exchange='', routing_key="project1_chanel1_queue1", body="THis is a First3 Massage")


chanel2.basic_publish(exchange='', routing_key="project1_chanel2_queue1", body="THis is a First Massage2")

chanel2.basic_publish(exchange='', routing_key="project1_chanel2_queue1", body="THis is a Tow Massage",
                      properties=pika.BasicProperties(content_type='text/plain', delivery_mode=1))

chanel3.basic_publish(exchange='', routing_key="project1_chanel3_queue3", body="THis is a First4 Massage")

connection_project1.close()

print("Finished")
