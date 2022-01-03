# Corn Engine Tools (Basically the middle kernel)
# Do not edit unless modding (ratio)
# made by Arezalgamer89
# under the MIT license
import random
import time
date = time # goes undercover as an module
import os
systemc = os # goes undercover as an module

debugState = "No" # Additional layer for indicating if debugVerbose Exists, first layer is on info.corndata

login_name = open('user/cornname')  # Your username
l_n = login_name.read() # Reads cornname

help = 'cetHELP.txt' # Used by Testers, Edit this if your help file is different

ce_tools_ver = "1.8.0" # used for testers and more func(s)

beatles_members = ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"] # A test Array

beatles_currentstate = ["Discontinued and dead"] # A meta test

bts_members = ["Jin", "RM", "Jungkook", "J-Hope", "Suga", "V", "Jimin"] # A test array 2
#dArray = []s
wrongInputTester = "Wrong Input or command!" # used for tests or the prompts

WrongPasswordText = "Wrong Password to" + l_n # (Unused) Used for login.py when you enter a wrong password


def randomNum(): #useful tool for returning a random number using i. n. t.
    print(random.randrange(0, 999999))
    # switched from int to range


def RequestHello():  # Gives out a Hello!
    dArray = input("") # Setup dArray for an input 
    if dArray == "Hello World":
        print("Hello Mister!")
    elif dArray == "Hello":
        print("Hello!")
    elif dArray == "Hi":
        print("Hi!")
    else:
        print("The Python Passes by without saying anything...")
    dArray = [] # Unsetup dArray after input is complete


def rollADice(): # Roll a dice between
    print("The dice landed on: ", random.randint(1, 6)) 

def debugFound(): # Used when our ce_tools is aware that we have him running on tester
    print("It seems you have me running on a tester")
    print("The filename is", systemc.__name__)
    input()
    print("I may also tell you that my version is", ce_tools_ver)
    input()
    print("Want me to open getHELP?")
    d = input("Y/N >>> ")
    if d == "y" or "Y" or "yes":
        systemc.startfile(help) # Universal
    elif d == "n" or "N" or "no":
        print("okay!")
    else:
        print("That wasn't a right answer ;(")