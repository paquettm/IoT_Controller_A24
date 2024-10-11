import paho.mqtt.client as mqtt

class IoT_Controller:
    client = None

    def configure():
        IoT_Controller.client = mqtt.Client()
        #pass the reference to the callback function to handle incoming messages
        IoT_Controller.client.on_message = IoT_Controller.on_message
        #must connect to the MQTT message broker at "localhost" on port 1883
        IoT_Controller.client.connect("localhost",1883)
#****************************************************************************
        # The topic wildcards to use when subscribing are
        # "+" for a single level, e.g., house/+ will catch house/temp but not /house/temp/room
        # "#" for a multiple levels, e.g., # will catch house/temp,  /house/temp/room, and bad/bad/cat
        #IoT_Controller.client.subscribe("*")
        IoT_Controller.client.subscribe("#")
#****************************************************************************

    def on_message(client, userdata, message):
        #this is where we handle the messages
        #Using try..except (exception handling)
        try:
            value = float(message.payload.decode("utf-8"))
        except ValueError:
            print("String")
            value = message.payload.decode("utf-8")
        topic = message.topic
        print(topic, value)

    def run():
        IoT_Controller.client.loop_forever()

def main():
    IoT_Controller.configure()
    IoT_Controller.run()

if __name__ == "__main__":
    main()
