def play():   
    print('------------------------------')
    print('Welcome to the Divination Game')
    print('------------------------------')
    
    secret_word = "banana"
    
    values = []
    for i in secret_word:
        values.append("_")

    hanged = False
    correct = False
    
    while (not hanged and not correct):
        letter = input("Type a letter: ").strip()

        index = 0;
        for l in secret_word:
            if (l.lower() == letter.lower()):
                print("Found ", l, "in position", index)
                values[index] = l
            index += 1 
        print(values)

    print("The end")

if(__name__ == "__main__"):
    play()