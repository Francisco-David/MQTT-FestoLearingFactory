from pyModbusTCP.client import ModbusClient
from pyModbusTCP.utils import test_bit

from time import sleep

c = ModbusClient(host="192.168.200.226", port=502, unit_id=1, auto_open=True)

while True:
    read_reg = c.read_holding_registers(8001, 1)
    if test_bit(read_reg[0], 0) == True:
        print("Sensor bit0 activated")

    sleep(1)