print('------------------------------')
print('Welcome to the Divination Game')
print('------------------------------')

secret_number = 42

guess = input("Type your number: ")

print('You typed', guess)

if (guess == secret_number):
    print('Congratulations, you win!')
else:
    print('U LOSE!')

print ("The End")