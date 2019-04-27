from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import sys,weakref
consumer = KafkaConsumer(
    # You should update the topic name like teb_topic
    'teb_topic',
     bootstrap_servers=['kafka:9092'],
     api_version=(0,10),
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('mongodb:27017')
collection = client.teb_topic.teb_topic

for message in consumer:
    message = message.value
    #print(message)
    #msg_json = json.loads(message.value)
    #teb2.insert_one(msg_json)
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))
    sys.stdout.write(str(message))