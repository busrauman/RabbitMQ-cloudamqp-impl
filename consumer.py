import pika, os, time

def pdf_process_function(msg):
  print(" PDF processing")
  print(" Received %r" % msg)

  time.sleep(5) # delays for 5 seconds
  print(" PDF processing finished");
  return;

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://zvyaduaw:1CH4GHjat6KC5L5X9R2G1clzv136CYUN@emu.rmq.cloudamqp.com/zvyaduaw')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess')  # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  pdf_process_function(body)

# set up subscription on the queue
channel.basic_consume(callback,
  queue='pdfprocess',
  no_ack=True)

# start consuming (blocks)
channel.start_consuming()
#connection.close()
