#RANDOM GOD KNOWS WHAT

print("Hello! Welcome to the game")
print("1.Red Door 2.Blue Door 3.Black Door")
choice=int(input("Enter your choice 1,2 or 3\n"))
if choice==1:
    print("Game over!\n")
elif choice==2:
    print("You deserve to lose!\n")
elif choice==3:
    print("yay You cleared the level!\n")
    print("Choose 1 or 2\n")
    choice2=int(input("Enter choice: \n"))
    if choice2==1:
        print("You lose, as a result of choosimg engineering\n")
    elif choice2==2:
        print("You have no other option other than losing")
    else:
        print("Dont try invalid option just give up")
else:
    print("Dont try invalid option just give up!")
