#Program to find  sum of all elements in list
def sumlist(list):
    sum=0
    for i in range(len(list)):
        sum = sum+list[i]
    return sum

list = [10, 9, 7, 5]

print("sum of list: ",sumlist(list))