from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")

topic = client.topics['sales_topic']

producer = topic.get_sync_producer()

producer.produce('Welcome in PyKafka 123'.encode('ascii'))
