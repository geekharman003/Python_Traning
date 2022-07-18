# st="madam"
# if st[::-1]==st:
#     print("palindrome")
# else:
#     print("not palindrome")



num=int(input("enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    if(temp==rev):
        print("number is palindrome")
    else:
        print("number is not palindrome")
        
        