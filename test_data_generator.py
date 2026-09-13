import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883)

topics = {
    'lab/temperature': (20, 30),  # Min, Max range
    'lab/humidity': (40, 80)
}

while (True):
#for _ in range(50):  # Generate 50 readings
    for topic, (min_val, max_val) in topics.items():
        value = random.uniform(min_val, max_val)
        client.publish(topic, f"{value:.2f}")
    time.sleep(2)  # Wait 2 seconds between readings

client.disconnect()
