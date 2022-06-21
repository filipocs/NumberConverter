roman = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, "X"), (5, "V"), (1, 'I')]

while True:

    try:
        decimal_number = int(input('Choose the number that you want to convert to ancient roman: '))
        if decimal_number < 1 or decimal_number > 3999:
            print('This number is unreachable in this program. For more information please read the readme.')
            continue
    except ValueError:
        print('This is not a Valid number!')
        continue

    roman_number = ""
    counter = 0
    number = decimal_number
    for r in roman:
        division = decimal_number // r[0]
        if division == 4:
            roman_number = roman_number + r[1] + roman[counter - 1][1]
            decimal_number -= division * r[0]
        elif division == 1 and decimal_number % r[0] == 4 and counter % 2 == 1:
            roman_number = roman_number + roman[counter + 1][1] + roman[counter - 1][1]
            decimal_number -= roman[counter + 1][0] - roman[counter - 1][0]
        elif 0 < division < 4:
            roman_number = roman_number + r[1] * division
            decimal_number -= division * r[0]
        counter += 1
    print(f'The number {number} in ancient roman numbers is {roman_number}\n')
    while True:
        answer = str(input('Do you wish to continue? [Y/N]')).capitalize()[0]
        if answer in 'YN':
            break
        else:
            print('This is not a Valid answer')
    if answer in 'N':
        break
