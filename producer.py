from confluent_kafka import Producer
import sys

print("Creating producer...")
conf = {
    'bootstrap.servers': "localhost:9092"
}
producer = Producer(conf)
print("Producer created...\n")

msg = sys.argv[1]
partition = 0 if msg[0] < "N" else 1
print("Name entered : " + msg)
print("Partition : " + str(partition) + "\n")


def delivery_callback(err, msg):
    if err:
        print('Message failed delivery: %s\n' % err)
    else:
        print('Message delivered to %s [%d] @ %d\n' % (msg.topic(), msg.partition(), msg.offset()))

print("Sending message...")
producer.produce(topic="Users", value=msg, partition=partition, callback=delivery_callback)
producer.flush()
print("Operation Successful")