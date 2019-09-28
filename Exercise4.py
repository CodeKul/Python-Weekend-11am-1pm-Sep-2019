# Write a function to conver binary to decimal number
# 1010 - 10
# (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0)
# 8 + 0 + 2 + 0
# 10

def bin_dec(no):
    deg = 0
    dec = 0
    while no > 0:
        dig = no % 10
        no = int(no / 10)
        dec = dec + (dig * 2**deg)
        deg += 1
    return dec

bin_no = int(input('Enter Binary no: '))
dec_no = bin_dec(bin_no)
print('Decimal:', dec_no)