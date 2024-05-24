
from paho.mqtt import publish
from time import sleep
from mqttDCI import *
from DistributionCenterInputModule import *
from paho.mqtt import subscribe

test = mqttDCI("192.168.200.226")

test.check_conveyor_output_piece_end()