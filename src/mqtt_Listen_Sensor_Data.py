# Escuta o topico base e chama sensor_Data_Handler para guardar o valor do payload
import paho.mqtt.client as mqtt
from store_Sensor_Data_to_DB import sensor_Data_Handler

# MQTT
MQTT_Broker = "host-name"
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = "topic-name"


# Se inscreve no topico base
def on_connect(mosq, obj, flags, rc):
    mqttc.subscribe(MQTT_Topic, 0)
    print "rc: "+str(rc)


# Caso receba uma menssagem salve no DB
def on_message(mosq, obj, msg):
    print "MQTT Data Received..."
    print "MQTT Topic: " + msg.topic
    print "Data: " + msg.payload
    sensor_Data_Handler(msg.topic, msg.payload)


def on_subscribe(mosq, obj, mid, granted_qos):
    pass


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Conecta ao broker
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Loop
mqttc.loop_forever()