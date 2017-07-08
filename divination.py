def game():
    number = input("Type your number: ")
    number = int(number)

    print('You typed', number)

    if (number == secret_number):
        print('Congratulations, you win!')
    else:
        if (number < secret_number):
            print('Wrong! Type a GREATER number! ')
            game()
        elif (number > secret_number):
            print('Wrong! Type a LOWER number!')
            game()

print('------------------------------')
print('Welcome to the Divination Game')
print('------------------------------')

secret_number = 42

game()