import os
import sys
import pika


def publish_websocket_message(amqp_url, message):
    print(f"Connecting to {amqp_url}")
    mq_creds = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(mq_creds)

    channel = connection.channel()

    channel.basic_publish(exchange="amq.topic",
                          routing_key="websocket",
                          body=message)
    connection.close()

    print(f"[x] Sent '{message}'")
    return 0


if __name__ == "__main__":
    amqp_url = os.environ.get("AMQP_URL", "amqp://user:password@localhost:5672/%2F")

    sys.exit(publish_websocket_message(
        amqp_url=amqp_url,
        message="Websocket message!"
    ))
