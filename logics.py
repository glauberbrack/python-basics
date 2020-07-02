"""
Logics Structures

Unique operators:
    - not, is
Binary operators:
    - and, or

To use "and", both values need to be True. When we use "or", just one of the values need to be True
"""

active = True
authenticated = True

if active and authenticated:
    print('Hi, there!')
else:
    print('You need to activate your account')
