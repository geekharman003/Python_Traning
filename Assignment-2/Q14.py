# Write a Python program to convert more than one list to nested dictionary. 
new_lis = ["student_name", 'id', 'age']

second_lis = ['Elon', '2345', '78']
third_lis = [23, 45, 91]
new_output = [{u: {v: w}} for (u, v, w) in zip(new_lis, second_lis, third_lis)]
print("Nested dictionary:",new_output) 