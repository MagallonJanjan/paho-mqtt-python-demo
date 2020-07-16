import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata,flags, rc):
    print("Connected with result code "+str(rc))
    
   
def on_message(client, userdata, msg):
    print(str(msg.payload.decode()))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("mqtt.eclipse.org", 1883, 60)

message = ''

while True:
    client.loop()
    message = input("Please Enter a Message: ")
    client.publish("joseph/sample", message)
   
