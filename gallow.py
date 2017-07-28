import random 

def play():   
    print('------------------------------')
    print('Welcome to the Divination Game')
    print('------------------------------')
    
    words = []
    file = open('words.txt', 'r')
    for line in file:
        words.append(line.strip())

    file.close()
    
    ind = random.randrange(0, len(words))    
    secret_word = words[ind].lower()
    
    values = ['_' for letter in secret_word]

    print (values)
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
                    values[index] = l
                index += 1
        else:
            wrongs -= 1
            print("Miss! U have {} tries".format(wrongs))
        
        hanged = wrongs == 0
        correct = '_' not in values

        word = str()
        for l in values:
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