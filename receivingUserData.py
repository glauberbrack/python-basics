"""
Receiving data from user
"""

# The example bellow use the 'print' from version 2.x of Python

# Input Data
# print("What's your name?")
# name = input()

name = input("What's your name?")


# Processing...

# Output Data
print('Hi, %s' % name)

# Input Data
# print("What's your age?")
# age = input()
age = int(input("What's your age"))

# Output Data
print('%s has %s years old' % (name, age))

"""
You need to use %s and the variable name after an %.
If you want to use more than one variable, you need to use parenthesis.

"""

# Now we can see an example that can be used since version 3.x
print('{0} has {1} years old'.format(name, age))

# The most updated 'print' form to be used, since version 3.7. You MUST pass the letter f in the begining.
print(f'{name} has {age} years old')

"""
int(age) => cast
Cast is a 'conversion' from an type of variable to another.
"""

print(f'{name} was born in {2020 - int(age)}')
