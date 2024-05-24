from pyModbusTCP.client import ModbusClient

from pyModbusTCP.utils import set_bit
from pyModbusTCP.utils import reset_bit

from time import sleep


c = ModbusClient(host="192.168.200.226", port=502, unit_id=1, auto_open=True)

write_reg = 0

while True:
    write_reg = set_bit(write_reg, 0)
    c.write_multiple_registers(8003, [write_reg])
    
    sleep(2)
    
    write_reg = reset_bit(write_reg, 0)
    c.write_multiple_registers(8003, [write_reg])

    sleep(2)

