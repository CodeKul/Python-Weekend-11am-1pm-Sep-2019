'''
Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6 
Digits 2
'''

string = input('Enter a string: ')
let_cnt = 0
dig_cnt = 0
spc_cnt = 0
for ch in string:
    if ch.isalpha():
        let_cnt += 1
    elif ch.isdigit():
        dig_cnt += 1
    else:
        spc_cnt += 1

print('Letter count:', let_cnt)
print('Digit count:', dig_cnt)
print('Special char count:', spc_cnt)