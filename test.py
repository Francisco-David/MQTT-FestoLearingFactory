from DistributionCenterInputModule import *
from paho.mqtt import publish

test = DistributionCenterInputModule("192.168.200.226")

n_pieces = 0


def seperator_func():
    test.seperator_main_reset()
    while not test.check_seperator_main_piece():
        sleep(0.5)
    test.seperator_main_set()
    sleep(0.2)


#Updates magazines 1-3
for i in range(1,4):
    if test.check_magazine_empty(i):
        publish.single("input2/mag"+str(i), "empty", hostname="192.168.200.161")
    else:
        publish.single("input2/mag"+str(i), "not_empty", hostname="192.168.200.161")

#Updates magazine 4
if test.check_magazine_4_empty:
    publish.single("input2/mag4", "empty", hostname="192.168.200.161")
else:
    publish.single("input2/mag4", "not_empty", hostname="192.168.200.161")



test.conveyor_main_right()
test.conveyor_output_forward()

while (not (test.check_magazine_4_empty()&test.check_magazine_empty(1)&test.check_magazine_empty(2)&test.check_magazine_empty(3))):

    #Sensors between magazines

    mag_id = randrange(1,5)
    if mag_id != 4:
        if not test.check_magazine_empty(mag_id):

            test.magazine_eject(mag_id)
            sleep(1)
            test.magazine_retract(mag_id)
            sleep(1)

            n_pieces+=1
            publish.single("input2/n_pieces_delivered", n_pieces, hostname="192.168.200.161")

        else:
            publish.single("input2/mag"+str(mag_id), "empty", hostname="192.168.200.161")

    else:
        if not test.check_magazine_4_empty():

            test.conveyor_side_on()
            sleep(1)
            
            test.seperator_side_set()
            sleep(1)
            test.seperator_side_reset()
            sleep(1)

            n_pieces+=1
            publish.single("input2/n_pieces_delivered", n_pieces, hostname="192.168.200.161")
            
        else:
            test.conveyor_side_off()
            sleep(1)

            publish.single("input2/mag4", "empty", hostname="192.168.200.161")

    #seperator_func

    #Sensor de validez + ejector

    #Separator_main

test.conveyor_main_stop()
test.conveyor_output_stop()