from mqttDCI import *
from DistributionCenterInputModule import *
from paho.mqtt import subscribe

test = mqttDCI("192.168.200.226")
test.work()


#test2 = DistributionCenterInputModule("192.168.200.226")
#test2.work()


