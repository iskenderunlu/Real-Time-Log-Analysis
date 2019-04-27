import os, sys, time
from time import sleep
import json
from json import dumps, loads
from kafka import KafkaProducer
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

name = "city_logs/app.log"
current = open(name, "r")
curino = os.fstat(current.fileno()).st_ino
#data =[]
datum = {}

while True:
    while True:
        buf = current.readline()
        if buf == "":
            break
        #sys.stdout.write(buf)
        buf_list = buf.split(" ")
        datum["log_date"] = buf_list[0] + " " + buf_list[1]
        datum["log_level"] = buf_list[2]
        datum["city"] = buf_list[3]
        datum["describtion"] = buf_list[4]
        #data.append(datum)
        producer.send('test44', datum)
        datum ={}
        
    try:
        if os.stat(name).st_ino != curino:
            new = open(name, "r")
            current.close()
            current = new
            curino = os.fstat(current.fileno()).st_ino
            continue
    except IOError:
        pass
    time.sleep(1)