# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
st = input("Input words: ")

new_st = st.split(",")
new_st.sort()
print((', ').join(new_st))