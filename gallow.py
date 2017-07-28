import random 
def welcome_message():
    print('------------------------------')
    print('Welcome to the Divination Game')
    print('------------------------------')
    
def choose_word():
    words = []
    file = open('words.txt', 'r')
    for line in file:
        words.append(line.strip())

    file.close()
    
    ind = random.randrange(0, len(words))    
    secret_word = words[ind].lower()
    return secret_word

def init_right_letters(word):
    return ['_' for letter in word]

def play():   
    welcome_message()
    
    secret_word = choose_word()

    right_letters = init_right_letters(secret_word)

    print (right_letters)
    hanged = False
    correct = False
    wrongs = 6

    while (not hanged and not correct):
        letter = input("Type a letter: ").strip().lower()

        index = 0;
        if (letter in secret_word):
            for l in secret_word:
                if (l == letter):
                    print("Found ", l, "in position", index)
                    right_letters[index] = l
                index += 1
        else:
            wrongs -= 1
            print("Miss! U have {} tries".format(wrongs))
        
        hanged = wrongs == 0
        correct = '_' not in right_letters

        word = str()
        for l in right_letters:
            word += l + " "

        print(word)
    if(correct):
        print("YOU ARE THE CHAMPION!!")
    else:
        print("YOU LOSE!!")
    print(secret_word)
    print("The end")

if(__name__ == "__main__"):
    play()