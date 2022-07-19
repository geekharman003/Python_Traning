def my_func(str1):
  new_str=""
  for i in range(len(str1)):
    if i%2==0:
     new_str=new_str+str1[i]
  return new_str
print(my_func("harman"))