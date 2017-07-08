print('------------------------------')
print('Welcome to the Divination Game')
print('------------------------------')

secret_number = 42

number = input("Type your number: ")
number = int(number)

print('You typed', number)

if (number == secret_number):
    print('Congratulations, you win!')
else:
    print('U LOSE!')

print ("The End")