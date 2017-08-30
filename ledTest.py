#! /usr/bin/env python

# GNU GPL V3
# Test code for 4tronix Picon Zero

import piconzero as pz, time


speed = 0.1
pz.init()
pz.setOutputConfig(0, 1)    
try:
    while True:
        pz.setOutput(0, 5) # 5% very dim
        time.sleep(speed)
        pz.setOutput(0, 30) # 30% medium
        time.sleep(speed)
        pz.setOutput(0, 70) # 70% bright
        time.sleep(speed)
        pz.setOutput(0, 100) # 100% maximum
        time.sleep(speed)
        pz.setOutput(0, 70) # 70% bright
        time.sleep(speed)
        pz.setOutput(0, 30) # 30% medium
        time.sleep(speed)
except KeyboardInterrupt:
    print
finally:
    pz.cleanup()

