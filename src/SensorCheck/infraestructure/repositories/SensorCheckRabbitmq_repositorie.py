import pika
import json
import os
from dotenv import load_dotenv

class RabbitMQRepository:
    def __init__(self):
        load_dotenv()  

        self.host = os.getenv("RABBITMQ_HOST", "localhost")
        self.port = int(os.getenv("RABBITMQ_PORT", 5672))
        self.username = os.getenv("RABBITMQ_USERNAME", "guest")
        self.password = os.getenv("RABBITMQ_PASSWORD", "guest")
        self.connection_params = None

        try:
            credentials = pika.PlainCredentials(self.username, self.password)
            self.connection_params = pika.ConnectionParameters(
                host=self.host,
                port=self.port,
                credentials=credentials,
                heartbeat=600,
                blocked_connection_timeout=300
            )
            print(f"Parámetros de conexión configurados: host={self.host}, port={self.port}")
        except Exception as e:
            print(f"Error configurando parámetros de conexión: {e}")

    def send_message(self, queue_name: str, message: str):
        connection = None
        try:
            json.loads(message)

            connection = pika.BlockingConnection(self.connection_params)
            channel = connection.channel()

            channel.queue_declare(queue=queue_name, durable=True)

            channel.basic_publish(
                exchange='',
                routing_key=queue_name,
                body=message.encode('utf-8'),
                properties=pika.BasicProperties(delivery_mode=2)
            )
            print(f"Mensaje JSON enviado a la cola '{queue_name}': {message}")

        except json.JSONDecodeError:
            print("Error: El mensaje no es un JSON válido.")
        except pika.exceptions.AMQPConnectionError:
            print("Error de conexión con RabbitMQ. Verifica si está corriendo y accesible.")
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
        finally:
            if connection and connection.is_open:
                connection.close()
                print("Conexión a RabbitMQ cerrada.")
