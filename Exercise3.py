# Write a function to conver decimal number to binary
# 10 - 1010

def dec_bin(no):
    bin = 0
    mul = 1
    while no > 0:
        dig = no % 2
        no = int(no / 2)
        bin = (mul * dig) + bin
        mul *= 10
    return bin

dec_no = int(input('Enter decimal no: '))
bin_no = dec_bin(dec_no)
print('Binary:', bin_no)