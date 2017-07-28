def play():   
    print('------------------------------')
    print('Welcome to the Divination Game')
    print('------------------------------')
    
    secret_word = "banana".lower()
    
    values = []
    for i in secret_word:
        values.append("_")

    print (values)
    hanged = False
    correct = False
    wrongs = 0

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
            wrongs += 1
        
        hanged = wrongs == 6
        correct = '_' not in values

        word = str()
        for l in values:
            word += l + " "

        print(word)
    if(correct):
        print("YOU ARE THE CHAMPION!!")
    else:
        print("YOU LOSE!!")
    print("The end")

if(__name__ == "__main__"):
    play()