import pika, os, logging
logging.basicConfig()

url = os.environ.get('CLOUDAMQP_URL', 'amqp://zvyaduaw:1CH4GHjat6KC5L5X9R2G1clzv136CYUN@emu.rmq.cloudamqp.com/zvyaduaw')
print(url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)  # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess')  # Declare a queue
# send a message

channel.basic_publish(exchange='', routing_key='pdfprocess', body='User information')
print ("[x] Message sent to consumer")
connection.close()
