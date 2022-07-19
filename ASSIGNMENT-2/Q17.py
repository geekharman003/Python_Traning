# Write a Python program to remove an empty tuple(s) from a list of tuples.
def delete(list1):
    list1= filter(None, list1)
    return list1
list1=[ (), ('harman'), (), ('4', '2','7',' '), (), ('8', '1'), ('0', '8') ]
print(delete(list1))