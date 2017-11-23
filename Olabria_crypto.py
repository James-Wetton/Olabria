import time
import os
import sys
import random

true = 1
while true == 1:
    try:
        aud = 1
        oad = 1 * aud

        id = input("Citizen id: ")
        if os.path.exists(id + '.txt'):
            f = open(id + '.txt', 'r')
            usersavings = str(f.readline())
            print('\n \n')
            print(usersavings + " oad savings in account")
            print('\n')
            f.close()
            func = input("press 1 to exchange, press 2 to enter tax mode, press 3 to add funds ")
            if func == ('1'):
                amount = input("How much would you like to exchange? ")
                userx = input("Please type the citizen id of the person to exchange with: ")
                f = open(userx + '.txt', 'r')
                savingsuserx = f.read()
                f.close()

                f = open(userx + '.txt', 'w')
                addition = int(savingsuserx) + int(amount)
                f.write(str(addition))
                f.close

                f = open(id + '.txt', 'w')
                deduct = int(usersavings) - int(amount)
                f.write(str(deduct))
                f.close

                print("transferred " + amount + " oad from " + id + " to " + userx)


            if func == ('2'):
                print("function doesnt exist ")

            if func == ('3'):
                addfund = input("Please type in admin code: ")
               

        else:
            print("no existing id")


    except KeyboardInterrupt:
        break
