def play():   
    print('------------------------------')
    print('Welcome to the Divination Game')
    print('------------------------------')
    
    secret_word = "banana"
    
    values = []
    for i in secret_word:
        values.append("_")

    print (values)
    hanged = False
    correct = False
    wrongs = 0
    
    while (not hanged and not correct):
        letter = input("Type a letter: ").strip()

        index = 0;
        if (letter not in secret_word):
            wrongs += 1
            if (wrongs == 6):
                hanged = True
                print("LOOOSER")
                break;
                
        for l in secret_word:
            if (l.lower() == letter.lower()):
                print("Found ", l, "in position", index)
                values[index] = l
            index += 1

        word = str();
        for l in values:
            word += l + " "

        print(word)

        if ('_' not in values):
            correct = True
            print("YOU WIN!!")

    print("The end")

if(__name__ == "__main__"):
    play()