#This file is to be run only once.

from confluent_kafka.admin import AdminClient, NewTopic

#Creating an admin client
admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092",
})

# Creating a new topic called user which has two partitions
# Names from A-M will be in Partition 1 
# Names from N-Z will be in Partition 2
topic_list = [NewTopic("Users", num_partitions=2, replication_factor=1)]
fs = admin_client.create_topics(topic_list)

for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))