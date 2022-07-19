str1=input("enter the string:")
str1=str1.split()
i=0
count=0
while i<len(str1):
 for j in str:
        if str[i]==j:
            count=count+1
            print(str[i],"present",count,"times") 
           
            i=i+1