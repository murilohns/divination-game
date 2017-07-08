def game():
    number = input("Type your number: ")
    number = int(number)

    correct = number == secret_number
    lower = number < secret_number
    greater = number > secret_number
    print('You typed', number)

    if (correct):
        print('Congratulations, you win!')
    else:
        if (lower):
            print('Wrong! Type a GREATER number! ')
            game()
        elif (greater):
            print('Wrong! Type a LOWER number!')
            game()

print('------------------------------')
print('Welcome to the Divination Game')
print('------------------------------')

secret_number = 42

game()