import time
import os
import sys
import random
import requests
taxamount = 49
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
            if '-' in usersavings:
                print("*** YOU ARE " + usersavings + " OAD IN DEBT ***")
            print('\n')
            f.close()
            func = input("press 1 to exchange, press 2 to enter tax mode, press 3 to add funds ")


            if func == ('1'):
                if int(usersavings) > 0:
                    amount = input("How much would you like to exchange? ")
                    if amount < int(usersavings):
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
                    else:
                        print("Selected amount higher than savings balance")
                else:
                    print("Not enough savings in account...")

            if func == ('2'):
                tax = input("This months tax is " + str(taxamount) + " oad. Ready to pay? ")
                if tax in ('Yes', 'Y', 'y', 'yes'):
                    if int(usersavings) > 50:
                        f = open(id + '.txt', 'w')
                        taxing = (int(usersavings) - int(taxamount))
                        f.write(str(taxing))
                        f.close()
                        f = open('fedgov.txt', 'r')
                        govamount = f.read()
                        f.close()
                        f = open('fedgov.txt', 'w')
                        govtaxation = int(govamount) + int(taxamount)
                        f.write(str(govtaxation))
                        f.close()
                        print("Completed the transaction.")
                    else:
                        print("Not enough savings in account. ")
                else:
                    print("Ok. Returning... ")

            if func == ('3'):
                addfund = input("Please type in admin code: ")
                if addfund == ('Olabriastate'):
                    print("making transaction...")
                    f = open(id + '.txt', 'w')
                    addedfunds = int(usersavings) + 100
                    f.write(str(addedfunds))
                    f.close()
                    print("transaction complete!")
                    print("You now have " + str(int(usersavings) + 100)  + " oad of savings in your account! ")
                else:
                    print("invalid code. Returning...")
        else:
            print("no existing id")
    except KeyboardInterrupt:
        break
