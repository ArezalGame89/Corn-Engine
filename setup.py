import os
import time
import random
with open('user/info.corndata', 'w') as f:
	f.writelines("1")



print("""

 ________  ________  ________  ________           ________  _______  _________  ___  ___  ________   
|\   ____\|\   __  \|\   __  \|\   ___  \        |\   ____\|\  ___ \|\___   ___\\  \|\  \|\   __  \  
\ \  \___|\ \  \|\  \ \  \|\  \ \  \\ \  \       \ \  \___|\ \   __/\|___ \  \_\ \  \\\  \ \  \|\  \ 
 \ \  \    \ \  \\\  \ \   _  _\ \  \\ \  \       \ \_____  \ \  \_|/__  \ \  \ \ \  \\\  \ \   ____\
  \ \  \____\ \  \\\  \ \  \\  \\ \  \\ \  \       \|____|\  \ \  \_|\ \  \ \  \ \ \  \\\  \ \  \___|
   \ \_______\ \_______\ \__\\ _\\ \__\\ \__\        ____\_\  \ \_______\  \ \__\ \ \_______\ \__\   
    \|_______|\|_______|\|__|\|__|\|__| \|__|       |\_________\|_______|   \|__|  \|_______|\|__|  
""")

name = input("Enter the username you want to use:   ")
pas = input("Enter your password:    ")

with open('user/cornname', 'w') as f:
	f.writelines(name)

with open('user/donotlook', 'w') as f:
	f.writelines(pas)

os.system('cls' if os.name=='nt' else 'clear') # stole this from pykern only because i couldn't figure out the if os thing
print("""



                                                                Setup is complete!


Loading...
""")

time.sleep(random.randint(0, 9))
os.system('cls' if os.name=='nt' else 'clear')
print("""



                                                                Setup is complete!


Done!
""")
time.sleep(2.0)
os.system('cls' if os.name=='nt' else 'clear')
print("""



                                                                Setup is complete!


Opening Login...
""")
time.sleep(0.5)
os.system('cls' if os.name=='nt' else 'clear')
print("Ok so in the next command, the plain normal 'login.py' shall appear, normally you should not see this message because it's supposed to clear after this")
os.startfile('login.py')