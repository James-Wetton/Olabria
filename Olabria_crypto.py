import time
import os
import sys
import random

true = 1
while true == 1:
    try:
        pip = 1
        olive = 100 * pip

        id = input("Citizen id: ")
        if os.path.exists(id + '.txt'):
            f = open(id + '.txt', 'r')
            lines = f.readlines()
            print(lines + "pips savings in account")

        else:
            print("no existing id")


    except KeyboardInterrupt:
        break
