"""
Repetition Structure (LOOP)

FOR Structure
    for item i interable
        // loop conditional
"""

name = "Glauber"
list = [1, 2, 3, 4, 5]
numbers = range(1, 10)

for word in name:
    print(word)

for n in list:
    print(n)

# In the example bellow, the last number will not be included
for n in range(1, 10):
    print(n)

# Using Enumerate
for i, v in enumerate(name):
    print(name[i])

# Letting the user choose the number of loops
quantity = int(input("How many times this loop must run?"))

for n in range(1, quantity+1):
    print(n)
