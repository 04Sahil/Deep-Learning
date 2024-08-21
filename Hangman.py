import random
#open textfile
f = open("word.txt","r")
#read file
data = f.readline()

#split words
word =  data.split()
word =random.choice(word)
#convert word to upper case
word = word.upper()
guessed_word = ""*len(word)
total_chances = 7
while total_chances != 0:
    print(guessed_word)
    letter = input("Guess a letter").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter :
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
        if guessed_word == word:
            print("Congratulations!You won")
            break
    else:
        total_chances -= 1
        print("Incorrect guess")
        print("the remaining guess are: ",total_chances)
else:
    print("Game over")
    print("You lost")
    print("All the chances are exaushted")








