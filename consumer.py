from confluent_kafka import Consumer, KafkaException


print("Creating consumer....")
conf = {
        'bootstrap.servers': "localhost:9092",
        'group.id': "test",
        'auto.offset.reset': "earliest"
}
consumer = Consumer(conf)
print("Consumer created...")


print("Subscribing to Users topic...")
def print_assignment(consumer, partitions):
    print('Assignment:', partitions)

consumer.subscribe(["Users"], on_assign=print_assignment)
print("Subscribtion complete...")

# Read messages from Kafka, print to stdout
try:
    while True: 
        msg = consumer.poll(timeout=1.0)

        if msg is None: 
            continue

        if msg.error():
            raise KafkaException(msg.error())
        else:
            #Print the received message
            print('%s [%d] at offset %d : %s' % (msg.topic(), msg.partition(), msg.offset(), msg.value()))

            # Store the offset associated with msg to a local cache.
            # Stored offsets are committed to Kafka by a background thread every 'auto.commit.interval.ms'.
            # Explicitly storing offsets after processing gives at-least once semantics.
            #consumer.store_offsets(msg)

except KeyboardInterrupt:
    print('Aborted by user\n')

finally:
    # Close down consumer to commit final offsets.
    consumer.close()