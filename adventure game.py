print("You are a Jewish man with your family in Nazi Germany hiding. The Gestapo has entered your house and is suspect of your helper. You must escape or there is a chance you and your family may die. What is your first choice?")
print("You can attempt to run or try to fight the Gustapo")
answer = input("your wife asks what to do your options are: Run, fight, Hide")
if(answer == "run"):
    print("You escape but leave your family behind")
    answer1 = input("Would you like to go to the city, country, or trainstation?")
    if(answer == "city"):
        print("You are captured")
        answer2 = input("You die")
    if(answer == "country"):
        print("You find somewhere to hide but have no food or shelter and night is approaching")
        answer3 = input("Would you like to try and find food or wait out the night")
    if(answer == "trainstation"):
        print("You are caught and taken by the gestapo")
        answer4 = input("You die")
        if(answer == "wait out night"):
            print("you survive but are very hungry")
            answer6 = input("you are desperate for food")
    elif(answer == "fight"):
    print("You beat up the men but your wife is injured")
    answer5 = input("semi-succesfu")
        elif(answer == "Hide"):
    print("You are found and taken by the gestapo, better luck next time")
        answer5 = input("Game over")

print()





