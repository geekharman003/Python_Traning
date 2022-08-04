try: 
    f = open("test.txt")
except: 
    print('Could not open file')
finally:
    f.close()

print('Program continue')