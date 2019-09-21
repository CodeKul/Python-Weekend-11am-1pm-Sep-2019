'''
    if condition:
        true statements
    else:
        false statements

    if condition:
        statements
    elif condition:
        statements
    else:
        statements
'''
a = 20
b = 20

if a < b:
    print('a is less than b')
else:
    print('a is greater than b')
    print('This is inside else')
print('This is outside else')


if a < b:
    print('a is less than b')
    if a == 10:
        print('a is equal to 10')
elif a == b:
    print('a and b are equal')
    if b == 20:
        print('b is equal to 20')
else:
    print('a is greater than b')

# Loops
