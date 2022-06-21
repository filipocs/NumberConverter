
base = 0
remainder = 0
numberlist =[]

def decimaltobinary(number):
    referencenumber = number
    while True:
        remainder = number % 2
        if number > 1:
            numberlist.append(remainder)
        else:
            pass
        number = number // 2
        if number < 2:
            numberlist.append(number)
            break
    newlist = list(reversed(numberlist))
    print(f' The decimal number {referencenumber} in binary base is ', end='')
    for n in newlist:
        print(n, end='')



def binarytodecimal(number):
    referencenumber = number
    decimal = 0
    sum = 0
    numberlist = [int(x) for x in str(number)]
    newlist = list(reversed(numberlist))
    for n in newlist:
        sum = sum + 2 ** decimal * n
        decimal += 1
    print(f' The binary number {referencenumber} in decimal base is {sum}')
