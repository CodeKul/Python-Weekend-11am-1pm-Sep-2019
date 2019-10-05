def calc_factorial(no):
    if no == 1:
        return no
    return no * calc_factorial(no - 1)
    
n = int(input('Enter a no: '))
fact = calc_factorial(n)

print('Factorial:', fact)