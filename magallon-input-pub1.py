import paho.mqtt.client as mqtt
import time

topic = input("Please Enter your topic: ")
payload =input("Please Enter payload: ")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print(" ")
   

client = mqtt.Client()
client.on_connect = on_connect

client.connect("mqtt.eclipse.org", 1883, 60)

time.sleep(1)
while True:
    client.loop()
    client.publish(topic, payload)
    time.sleep(1)