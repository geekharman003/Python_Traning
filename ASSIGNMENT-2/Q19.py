# Write a Python program to check the validity of a password (input from users)
import re
pas= input("Input your password")
x = True
while x:  
    if (len(pas)<6 or len(pas)>12):
        break
    elif not re.search("[a-z]",pas):
        break
    elif not re.search("[0-9]",pas):
        break
    elif not re.search("[A-Z]",pas):
        break
    elif not re.search("[$#@]",pas):
        break
    elif re.search("\s",pas):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")