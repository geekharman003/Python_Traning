# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ",nums)
print("\nAverage :\n",average_tuple(nums))
