# Simple Hello World to Apache Kafka 

## Introduction
- Using the kafka python client to setup topic, partitions, producers and consumers.
- Using the kafka python client to produce and consume messages.

---

## Prerequisites
You will need to:
- Install [Docker Desktop](https://docs.docker.com/desktop/) and make sure you have Docker Compose
- Install [Python 3](https://www.python.org/downloads/)

---

## Setup

### Step 1: Clone the current repository

```bash
$ git clone https://github.com/adityam31/hello-kafka.git
$ cd hello-kafka
```

### Step 2: Install python dependencies
*Note - You can also create a [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) beforehand*
```bash
$ pip install -r requirements.txt
```

### Step 3: Setup Zookeeper and Kafka
- Set up Zookeeper and Kafka via Docker using the below command and keep this terminal window active.

```bash
$ cd setup
$ docker compose up
```

*Note : You can also use the -d flag with docker compose command without needing to keep this terminal alive. But for looking at the Kafka logs, its better to keep this running in a separate window.*

### Step 4: Run the setup.py file
- Open up a new terminal window in setup folder and run setup.py only once to create a "Users" topic in kafka with two partitions.

```bash
$ python setup.py
```

---

## Running the Project

- Open up three new terminal windows
    - In the first window, we will produce messages by running producer.py
    - In the second window, we will run our first consumer by running consumer.py
    - In the third window, we will run second cosumer by running consumer.py here too

### producer.py
- This program will take a command line argument for *UserName* and will send this username as message to the "Users" topic in Kafka Broker.
    - If the first letter of the user name is within "A-M", it will send the message to partition 0.
    - If the first letter of the user name is within "N-Z", it will send the message to partition 1.

```bash
$ python producer.py Aditya
$ python producer.py Tirthraj
$ python producer.py Jitendra
```

### consumer.py
- The consumers run a infinite loop and have subscribed to the "Users" topic.
    - If you have created only one consumer, it will be assigned both partitions.
    - If you have created two consumers (as mentioned above), each consumer will assume responsibility of one of the partitions.
- As and when the producer produces a message, you can see it getting logged by the respective consumer.

```bash
$ python consumer.py
```

## Tearing down the application
### Step 1: Stop the consumers
- After you have finished running the entire project, you can shut down the consumers by pressing *Ctrl + C* in their respective terminals.

### Step 2: Stop Zookeeper and Kafka
- Exit the docker compose up command similarly by pressing *Ctrl + C*. 
- Stop & remove containers by running the following command - 

```bash
$ docker compose down
```

---

## Useful links and References
- Kafka : 
    - Kafka Docs : https://kafka.apache.org/documentation/
    - Kafka Introduction by Hussein Nasser : https://www.youtube.com/watch?v=R873BlNVUB4
    - Kafka Consumer Auto Offset Reset (Medium) : https://medium.com/lydtech-consulting/kafka-consumer-auto-offset-reset-d3962bad2665

- Python :
    - Kafka Python Client : https://docs.confluent.io/kafka-clients/python/current/overview.html 
    - Kafka Python Client Docs : https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html
    - Kafka Python Client Github (Examples) : https://github.com/confluentinc/confluent-kafka-python/tree/master/examples

- Docker
    - Setting up Kafka with docker : https://developer.confluent.io/quickstart/kafka-docker/

    