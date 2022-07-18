str="restart"
first_char=str[0]
str=str.replace(first_char,'$')
str=first_char+str[1:]
print(str)



