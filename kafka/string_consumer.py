from kafka import KafkaConsumer

consumer = KafkaConsumer(
  bootstrap_servers=["localhost:19092"],
  group_id="demo-group",
  auto_offset_reset="earliest",
  enable_auto_commit=True,
  consumer_timeout_ms=100
)
consumer.subscribe("orders")

try:
    for message in consumer:
        topic_info = f"topic: {message.partition}|{message.offset})"
        message_info = f"key: {message.key}, {message.value}"
        print(f"{topic_info}, {message_info}")
except Exception as e:
    print(f"Error occurred while consuming messages: {e}")
finally:
    consumer.close()
