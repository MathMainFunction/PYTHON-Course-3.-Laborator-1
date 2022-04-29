# I didn’t think that the task would be for linear algorithms
# Pleasantly surprises

value = int(input("Enter the three-digit number: "))

if (value <= 999):

    number1 = value // 100
    number2 = value % 100 // 10
    number3 = value % 10

    print('[1] =', number1, '[2] =', number2, '[3] =', number3)
    print('[Sum] =', number1 + number2+ number3)

else:

    print('[!] You entered a number greater than three digits')

# if/else - used for code beauty
# I know that it is possible to solve this problem through divmode
