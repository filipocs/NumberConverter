base = 0
remainder = 0
numberlist =[]

def decimaltooctal(number):
    referencenumber = number
    while True:
        remainder = number % 8
        if number > 1:
            numberlist.append(remainder)
        else:
            pass
        number = number // 8
        if number < 8:
            numberlist.append(number)
            break
    newlist = list(reversed(numberlist))

    print(f' The decimal number {referencenumber} in octal base is ', end='')
    for n in newlist:
        print(n, end='')

def octaltodecimal(number):
    referencenumber = number
    octal = 0
    sum = 0
    numberlist = [int(x) for x in str(number)]
    newlist = list(reversed(numberlist))
    for n in newlist:
        sum = sum + 8 ** octal * n
        octal += 1
    print(f' The octal number {referencenumber} in decimal base is {sum}')


