import paho.mqtt.client as mqtt
import examon_collector

def publish_to_examon(live_data):

    # MQTT broker settings
    MQTT_BROKER = 'test.mosquitto.org'  # e.g., 'localhost' or 'test.mosquitto.org'
    MQTT_PORT = 1883
    MQTT_USERNAME = 'your_username'  # if authentication is required
    MQTT_PASSWORD = 'your_password'  # if authentication is required

    # Create an MQTT client instance
    client = mqtt.Client()

    # Set username and password if required
    # client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    # Connect to the MQTT broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Start the network loop in a separate thread
    client.loop_start()

    try:
        # Use the function and publish each line
        for line in examon_collector.json_to_examon_data_model(live_data):
            topic, message = examon_collector.parse_line(line)
            if topic and message:
                # Publish the message to the MQTT broker
                client.publish(topic, payload=message)
                print(f'Published to topic: {topic}, message: {message}')
            else:
                print(f'Failed to parse line: {line}')
    finally:
        # Stop the network loop and disconnect
        client.loop_stop()
        client.disconnect()
