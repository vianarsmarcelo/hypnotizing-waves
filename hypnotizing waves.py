"""
Mesmerizing Waves
Displays a line of asterisks sliding continuously between left and right
in the terminal at 0.1-second intervals.
"""

import time

def decrease():
    for i in range(5, 0, -1):
        # print('i = ' + str(i))
        print(i * " " + "********")
        time.sleep(0.1)

def increase():
    for i in range(0, 5):
        # print('i = ' + str(i))
        print(i * " " + "********")
        time.sleep(0.1)

while True:
    decrease()
    # print("increase")
    increase()
