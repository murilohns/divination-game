from random import randint

print('------------------------------')
print('Welcome to the Divination Game')
print('------------------------------')

secret_number = randint(0, 100)
tries = 0
chances = 0

level = input("Choose the Dificulty: 1- Easy, 2- Normal, 3- Hard, 4- GOD")
level = int(level)

if (level == 1):
    chances = 10
elif (level == 2):
    chances = 5
elif (level == 3):
    chances = 3
else:
    chances = 1

for tries in range (1, chances + 1):
    print("Try {} of {}".format(tries, chances))
    number = input("Type your number: ")
    number = int(number)

    if(number < 1 or number > 100):
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
print("The secret number is:", secret_number)
print("The end")