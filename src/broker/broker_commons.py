import pika
from dataclasses import dataclass
from configs.config import BROKER_HOST, BROKER_PORT


@dataclass
class BrokerCommons:

    host: str = BROKER_HOST
    port: str = BROKER_PORT

    def __post_init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port, heartbeat=600))
    
    def queue_declare(self, queue: str):
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue, durable=True)

    def set_callback_function(self, function):
        self.callback = function

    def consume(self, queue: str):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=queue, on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()

    def send(self, queue: str, message: str):
        self.channel.basic_publish(exchange='', routing_key=queue, body=message)

    def close_connection(self):
        self.connection.close()
