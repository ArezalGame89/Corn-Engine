print("""

 ________  ________  ___       ________  ___  ___  ___       ________  _________  ________  ________     
|\   ____\|\   __  \|\  \     |\   ____\|\  \|\  \|\  \     |\   __  \|\___   ___\\   __  \|\   __  \    
\ \  \___|\ \  \|\  \ \  \    \ \  \___|\ \  \\\  \ \  \    \ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \   
 \ \  \    \ \   __  \ \  \    \ \  \    \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \\\  \ \   _  _\  
  \ \  \____\ \  \ \  \ \  \____\ \  \____\ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \\\  \ \  \\  \| 
   \ \_______\ \__\ \__\ \_______\ \_______\ \_______\ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\|_______|\|_______|\|_______|\|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|
                                                                                                         
                                                                                                         
                                                                                                         


[1] +
[2] -
[3] x
[4] /
""")
while True:
    select = input("> ")
    
    if select == '1':
        a = input("First number:  ")
        print("Plus")
        b = input('Second Number:  ')
        c = int(a)+int(b)
        print(c)

    if select == '2':
        a = input("Enter First Digit: ")
        print("-")
        b = input('Enter The Second Digit: ')
        c = int(a)-int(b)
        print(c)
        
    if select == '3':
        a = input("Enter First Digit: ")
        print("x")
        b = input('Enter The Second Digit: ')
        c = int(a)*int(b)
        print(c)

    if select == '4':
        a = input("Enter First Digit: ")
        print("/")
        b = input('Enter The Second Digit: ')
        c = int(a)/int(b)
        print(c)