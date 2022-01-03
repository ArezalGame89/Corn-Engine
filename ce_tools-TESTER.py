####################################################=
###################CE_TOOLS TEST####################
####################################################=
# A functional tester for the famous Corn Engine Utillity "CE_tools.py"
# This can also be used as a template on how to make a tester correctly
import ce_tools
from ce_tools import debugFound, systemc

systemc.system("cls" if systemc.name=='nt' else 'clear')
print("Corn Engine Tools Tester (CE_tools.py)")
print("This tools tests all functions up to", ce_tools.ce_tools_ver)

while True:
    poop = input("Where would you like to go?: ")
    if poop == "help":
        systemc.startfile(ce_tools.help)
    elif poop == "randomNum":
        print("This define prints a random number")
        print("using random randint between 0 to infinity")
        ce_tools.randomNum()
    elif poop == "request hello":
        print("this program says hi to you in different ways")
        print("Check out cetHelp.txt for more info on that")
        ce_tools.RequestHello()
    elif poop == "roll a dice":
        print("The dice function rolls a random dice")
        ce_tools.rollADice()
    elif poop == "exit":
        SystemExit()
    elif poop == "Debug":
        ce_tools.debugFound() # exclusive for testers only
    else:
        print(ce_tools.wrongInputTester) # uses the text from ce_tools