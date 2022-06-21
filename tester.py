from Binary import binarytodecimal,decimaltobinary
from octal import octaltodecimal,decimaltooctal


while True:
    print("This program convert decimal and binary numbers.\n"
        "[1] Convert a binary number to decimal number\n"
        "[2] Convert a decimal number to binary number\n"
        "[3] Convert an octal number to decimal number\n"
        "[4] Convert a decimal number to octal number\n")
    print('#' * 40)
    while True:
        try:
            menu = int(input("Choose a number: "))
            break
        except ValueError:
            print('Choose a Valid Option!')
    if menu > 0 and menu < 5:
        while True:
            try:
                number = int(input('Choose a number to convert: '))
                break
            except:
                print('Choose an Integer Number!')
        if menu == 1:
            binarytodecimal(number)
        elif menu == 2:
            decimaltobinary(number)
        elif menu == 3:
            octaltodecimal(number)
        elif menu == 4:
            decimaltooctal(number)
    else:
        print('Choose a Valid Answer!')

        #Error with a not valid number



    print()
    answer = str(input("Do you want to convert another number? [Y/N]"))
    answer = answer.capitalize()[0]
    if answer == "N":
        break
    else:
        print()
        print()
        continue

"""Thanks for using my project. The objective is that I try to use Python with small projects and to eventually
      work with programming, so this is the first project that i am doing by myself without no much search, and even
      that i know that exists a 1 line code to do this I tried just to practice logic """