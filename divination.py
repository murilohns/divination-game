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

    if(number < 0 or number > 100):
        print("Please, type a number between 1 and 100.")
        continue

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