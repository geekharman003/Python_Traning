# Write a Python program to remove the nth index character from a nonempty string. 
def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
string=input("Enter the sring:")
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))