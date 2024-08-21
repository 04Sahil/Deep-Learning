import random
while True:
    n = input("what is your name?")
    print("best of luck",n)
    word = ("girrafe", "colour","sahil","vansh","vaidehi","it")
    word = random.choice(word)
    guess = ""
    count = 1
    while guess != word :
        guess = input("Enter the word")
        if guess == word:
            print("You got it")
        else:
            print("Try again")
            count += 1
    print("Total",count,"guesses taken")


