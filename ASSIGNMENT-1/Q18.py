# Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. 
def three(str):
	return str[:3] if len(str) > 3 else str

print(three('ipy'))
print(three('python'))
print(three('py'))
