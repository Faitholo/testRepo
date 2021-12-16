import re
with open('C:/Users/ayara/fullname.txt') as f:
    contents = f.read().split()
    print("First name:", contents[0])
    print("Middle name:", contents[1])
    print("Last name:", contents[2])
