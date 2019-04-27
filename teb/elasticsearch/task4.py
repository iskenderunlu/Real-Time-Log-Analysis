from kafka import KafkaConsumer
from json import loads
import sys,weakref
from datetime import datetime
from elasticsearch import Elasticsearch

consumer = KafkaConsumer(
     # You should update the topic name like teb_topic
    'teb_topic',
     bootstrap_servers=['localhost:9092'],
     api_version=(0,10),
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

es = Elasticsearch()

i=0
print("before for")
for message in consumer:
    message = message.value
    res = es.index(index="test-index", doc_type='log', id=i, body=message)
    #print(res['result'])
    res = es.get(index="test-index", doc_type='log', id=i)
    print(res['_source'])
    sys.stdout.write(res['_source'])
    i = i + 1
    es.indices.refresh(index="test-index")

    if i == 10:
        break

#res = es.search(index="test-index", body={"query": {"match_all": {}}})
#print("Got %d Hits:" % res['hits']['total'])
#for hit in res['hits']['hits']:
#    print("%(log_date)s %(author)s: %(text)s" % hit["_source"])
#    sys.stdout.write(str(message))