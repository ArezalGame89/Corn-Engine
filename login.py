import os
from random import random
import time

login_pass = open('user/donotlook') # this is password
login_name = open('user/cornname')
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

while True:
	if l_n == '':
		log = input("eeeeeeeeeeeeeeeeeenter the passsssssssssssssssssssssssssssssssssssssssssssword to n o  thi ng ness  h h e erererere")
		print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
		time.sleep(1)
	log = input("Enter Password To " + l_n + " To Login: ")

	if log == l_p:
		print("Opening Home Page...")
		time.sleep(0.5)
		os.startfile("home.py")
		break

	else:
		if l_p == '':
			print('you have no password')
			time.sleep(random.randint(0.1, 90))
		else:
			print("Wrong Password To " + l_n)