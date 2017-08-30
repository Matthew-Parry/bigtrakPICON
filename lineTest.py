#! /usr/bin/env python
#
# Basic test of 3 way ryantec line tracker sensor on Picon Zero

import threewaylinetracker as line, time

line.init()

try:
    while True:
        left = int(line.getLeft())
        print "Left:", left
        right = int(line.getRight())
        print "Right:", right
        time.sleep(1)
except KeyboardInterrupt:
    print
finally:
    line.cleanup()

