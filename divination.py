print('------------------------------')
print('Welcome to the Divination Game')
print('------------------------------')

chances = input("Digite a quantidade de chances: ")
chances = int(chances)
secret_number = 42
tries = 0

for tries in range (1, chances + 1):
    print("Try {} of {}".format(tries, chances))
    number = input("Type your number: ")
    number = int(number)

    correct = number == secret_number
    lower = number < secret_number
    greater = number > secret_number

    print('You typed', number)

    if (correct):
        print('Congratulations, you win!')
        break;
    else:
        if (lower):
            print('Wrong! Type a GREATER number! ')
        elif (greater):
            print('Wrong! Type a LOWER number!')