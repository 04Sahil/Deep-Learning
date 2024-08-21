import random
print("Winning rules for rock paper scissor are:\n "
      +"rock vs scissor -> rock wins \n "
      +"rock vs paper -> paper wins\n"
      +"paper vs scissor -> scissor wins\n")

while True:
    print("Enter your choice \n 1 - rock \n 2 - paper \n 3-scissor")
    choice = int(input("enter your choice"))
    while choice > 3 or choice < 1 :
        choice = int(input("enter your choice"))
    
    if choice == 1:
        choice_name = "rock"
    elif choice == 2:
        choice_name = "paper"
    else :
        choice_name == "scissor"
    print("your choice is: ",choice)
    print("Now its computer's turn....")
    
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
    
    if comp_choice == 1:
        comp_choice_name = "rock"
    elif comp_choice == 2:
        comp_choice_name = "paper"
    else :
        comp_choice_name = "scissor"

    print("Computer choice is: ",comp_choice_name)
    print(choice_name,"Vs",comp_choice_name)
    
    if choice == comp_choice :
        print("its a draw",end="")
        result = "draw"
    if choice == 1 and  comp_choice== 2:
        print("you lost",end="")
        result = "lost"
    elif choice ==2 and comp_choice==3 :
        print("you lost",end="")
        result = "lost"
    if choice == 1 and comp_choice == 3:
        print("you win",end="")
        result = "win"
    elif choice == 2 and comp_choice == 1 :
        print("you win",end="")
        result = "win"
    if choice == 3 and comp_choice == 2 :
        print("you win",end="")
        result = "win"
    elif choice == 3 and comp_choice == 1 :
        print("you lost",end="")
        result = "lost"
    if result == "draw" :
        print("it's a tie")
    elif result == "lost":
        print(" Computer wins...")
    else:
        print("user wins...")
    print("Do you want to continue?(Y/N)")
    ans = input().lower
    if ans == "n":
        break

print("Thanks for playing")
        







