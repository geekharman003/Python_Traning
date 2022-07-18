str1,str2='abc','xyz'
temp=str1[0:2]
new_str1=str2[0:2]+str1[2:]
new_str2=temp+str2[2:]
print(new_str1+" "+new_str2)
