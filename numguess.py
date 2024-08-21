import random
while True:
    flag = True
    while flag:
        a = input("Enter the upper number")
        if a.isdigit():
            a = int(a)
            flag = False
        else:
            print("Invalid number! TRY Again")
          

    r = random.randint(1,a)
    guess = None
    count = 1

    while guess != r :
        guess = input("Type a number between 1 and"+ str(a)+":")
        if guess.isdigit():
            guess = int(guess)
        if guess == r :
            print("you got it")
        else:
            print("Try again")
            count += 1 
            
    print("Total" ,count, " guesses is taken")

