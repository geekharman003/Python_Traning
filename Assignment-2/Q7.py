# Python program to check the given year is leap or not
 
n = input("Please enter year")
 
year = int (n)
 
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)