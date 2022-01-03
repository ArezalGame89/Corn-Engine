import os
from random import random
import time
from tkinter.constants import END
import ce_tools
utils = ce_tools

login_pass = open('user/donotlook') # this is password
login_name = open('user/cornname')  # Your username
l_p = login_pass.read()
l_n = login_name.read()
print("""
 ___       ________  ________  ___  ________      
|\  \     |\   __  \|\   ____\|\  \|\   ___  \    
\ \  \    \ \  \|\  \ \  \___|\ \  \ \  \\ \  \   
 \ \  \    \ \  \\\  \ \  \  __\ \  \ \  \\ \  \  
  \ \  \____\ \  \\\  \ \  \|\  \ \  \ \  \\ \  \ 
   \ \_______\ \_______\ \_______\ \__\ \__\\ \__\
    \|_______|\|_______|\|_______|\|__|\|__| \|__|
""")


        
log = input("Enter Password To " + l_n + " To Login: ")
if log == l_p:
	print("Opening Home Page...")
	utils.date.sleep(1)
	utils.systemc.startfile("home.py")
        
        # Removed Wrong Password Text because
        # It just errors that im inconsistent in using the indents and spaces
exit()     
