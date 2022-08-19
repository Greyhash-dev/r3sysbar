import paho.mqtt.client as mqtt
broker_address="mqtt.realraum.at"

class r3_mqtt:
    def __init__(self):
        self.client = mqtt.Client("P1")
        self.client.connect(broker_address)
        self.basiclight_status = [0, 0, 0, 0, 0, 0]

    def panic(self):
        self.client.publish("realraum/pillar/boredoombuttonpressed", 1)

    def switch_basic(self, num):
        self.client.publish(f"action/GoLightCtrl/basiclight{num}", "on" if not self.basiclight_status[num] else "off")
        self.basiclight_status[num] = not self.basiclight_status[num]

    def all_basic_lights_on(self):
        for num in range(1, 7):
            self.client.publish(f"action/GoLightCtrl/basiclight{num}", "on")

    def all_basic_lights_off(self):
        for num in range(1, 7):
            self.client.publish(f"action/GoLightCtrl/basiclight{num}", "off")
