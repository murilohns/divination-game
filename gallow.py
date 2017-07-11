def play():   
    print('------------------------------')
    print('Welcome to the Divination Game')
    print('------------------------------')
    
    secret_word = "banana"
    hanged = False
    correct = False
    
    while (not hanged and not correct):
        letter = input("Type a letter: ").strip()

        index = 0;
        for l in secret_word:
            if (l.lower() == letter.lower()):
                print("Found ", l, "in position", index)
            index += 1 

    print("The end")

if(__name__ == "__main__"):
    play()