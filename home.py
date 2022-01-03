import sys
import time
import os
import socket
import boot
import ce_tools
# import korn
# import login
# from tkinter import * 
from tkinter import filedialog

login_pass = open('user/donotlook') #just in case, this is your password
login_name = open('user/cornname')
l_p = login_pass.read()
l_n = login_name.read()
print("""
 ________  ________  ________  ________           _______   ________   ________  ___  ________   _______      
|\   ____\|\   __  \|\   __  \|\   ___  \        |\  ___ \ |\   ___  \|\   ____\|\  \|\   ___  \|\  ___ \     
\ \  \___|\ \  \|\  \ \  \|\  \ \  \\ \  \       \ \   __/|\ \  \\ \  \ \  \___|\ \  \ \  \\ \  \ \   __/|    
 \ \  \    \ \  \\\  \ \   _  _\ \  \\ \  \       \ \  \_|/_\ \  \\ \  \ \  \  __\ \  \ \  \\ \  \ \  \_|/__  
  \ \  \____\ \  \\\  \ \  \\  \\ \  \\ \  \       \ \  \_|\ \ \  \\ \  \ \  \|\  \ \  \ \  \\ \  \ \  \_|\ \ 
   \ \_______\ \_______\ \__\\ _\\ \__\\ \__\       \ \_______\ \__\\ \__\ \_______\ \__\ \__\\ \__\ \_______\
    \|_______|\|_______|\|__|\|__|\|__| \|__|        \|_______|\|__| \|__|\|_______|\|__|\|__| \|__|\|_______|
                                                                                                             
""")
 
print("Welcome " + l_n)
	
print("Date: " + ce_tools.date.strftime("%m/%d/%y"))
print("If you're a beginner, type 'help'")

select = input("python3@" + l_n + "> ")

if select == 'help':
	print("""
1 To Open a Virtual Browser
2 To Open CE Text Editor
3 To Open File Opener
4 To Configure and Open BIOS
5 To Open Terminal
6 To Open The Calculator
7 To Close with Safety
	""")
if select == '1':
	os.startfile('home.py')
	os.startfile('brows.py')

if select == '2':
	os.startfile('home.py')
	os.startfile('edit.pyw')

#if select == '3':
	#os.startfile('home.py')
	#os.startfile('file.pyw')

if select == '4':
	while True:
		b_login = input(str("Please Enter The Password To " + l_n + " To Open BIOS: "))
		if b_login == l_p:
			print("Opening BIOS")
			host_name = socket.gethostname()
			host_ip = socket.gethostbyname(host_name)
			print("[1] USER NAME: " + l_n)
			print("[2] PASSWORD: " + l_p)
			print("Hostname:", host_name)
			print("Socket Local IPs: " + host_ip)
			edit_b = input("Enter number to change setting: ")
			if edit_b == '1':
				edit_n = input("Enter New Username: ")
				with open('user/dataname.pass', 'w') as f:
					f.writelines(edit_n)
				print("Username Changed To " + edit_n)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')

			if edit_b == '2':
				edit_p = input("Enter New Password: ")
				with open('user/password.pass', 'w') as f:
					f.writelines(edit_p)

				print("Password Changed To " + edit_p)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')
			else:
				print(ce_tools.WrongPasswordText)

	else:
		print("Wrong Password To " + l_n)

if select == '5':
	os.startfile('home.py')
	os.startfile('terminal.py')

if select == '6':
	os.startfile('home.py')
	os.startfile('calc.py')

if select == '7':
	os.system('exit')

if select == '3':
	filepath = filedialog.askopenfilename(initialdir="/",title="Open file",filetypes= (("text files","*.txt"),("all files","*.*")))
	os.startfile(filepath)


