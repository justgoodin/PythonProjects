from translator import translate

#User I/O
word = input("Enter the word: ")

while True:
    output = translate(word)
    if output[0] == False:
        i = 1
        print(f"{word} means:")
        for item in output[1]:
            print(f"{i}. {item}")
            i += 1
        break
    else:
        print(f"Did you mean \"{output[1]}\"?")
        print("Enter Y for yes, R to Retry, any other key to exit: ",end="")
        similar = input().strip()
        if similar == "Y" or similar == "y":
            output[0] = False
            word = output[1]
        elif similar =="R" or similar == "r":
            print("Enter the correct word: ",end="")
            word = input().strip()
        else:
            print("Exiting")
            break