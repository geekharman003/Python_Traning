# Patterns Program In Python
# rows = int(input('Enter the number of rows'))

# for i in range(rows):
#     for j in range(i):
#         print(i, end=' ')
#     print('')

# Inverted pyramid pattern of numbers
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
