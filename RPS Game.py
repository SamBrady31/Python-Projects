# make use of random choice function and delay computer answer a few seconds
import random, time

# keep score. add +1 to user_score if result is positive. add +1 to computer_score if result is positive. nothing if tied
user_score = 0
computer_score = 0
wager = 'n'
result = None

# Options to choose from
options = ("Rock", "Paper", "Scissors")

# HERE COMES THE GAMBLING CODE BABYYYYYY





# make the game replayable
while True:
    if user_score > 1:
        wager = input("Would you like to double or nothing your points this round? (Y?N) ")
        wager = wager.lower()


    # ask user for choice
    user_choice = input("Hi! Are you choosing Rock, Paper or Scissors? ")
    user_choice = user_choice.capitalize()

    # 8/11/22 7:03pm (tracey just dropped off flowers for fanny) - stupidly found this code below to work??!!?!?!?
    # AFTER WRITING AND DELETTING SO MUCH MOREEEEE
    if user_choice not in options:
        print("Real guess please asshole")
        time.sleep(0.5)
        continue


    # get random choice from computer and delay answer
    computer_choice = random.choice(options)
    print("Computer chooses.....")
    print(computer_choice)

    time.sleep(0.5)

    # determine the result
    if user_choice == computer_choice:
        print("You tied!")
        result = "Tie"
    elif user_choice == ("Scissors") and computer_choice == ("Rock"):
        print("You Lose SUCKAAA")
        result = "Lose"
        if wager == "y" and result == "Lose":
            user_score = user_score - user_score
        computer_score += 1
    elif user_choice == ("Rock") and computer_choice == ("Paper"):
        print("You Lose SUCKAAA")
        result = "Lose"
        if wager == "y" and result == "Lose":
            user_score = user_score - user_score
        computer_score += 1
    elif user_choice == ("Paper") and computer_choice == ("Scissors"):
        print("You Lose SUCKAAA")
        result = "Lose"
        if wager == "y" and result == "Lose":
            user_score = user_score - user_score
        computer_score += 1
    elif user_choice == ("Paper") and computer_choice == ("Rock"):
        print("You Win!")
        result = "Win"
        if wager == "y" and result == "Win":
            user_score = user_score * 2
        else:
            user_score += 1
    elif user_choice == ("Rock") and computer_choice == ("Scissors"):
        print("You Win!")
        result = "Win"
        if wager == "y" and result == "Win":
            user_score = user_score * 2
        else:
            user_score += 1
    elif user_choice == ("Scissors") and computer_choice == ("Paper"):
        print("You Win!")
        result = "Win"
        if wager == "y" and result == "Win":
            user_score = user_score * 2
        else:
            user_score += 1


    print("The score is currently "+str(user_score) + " to "+str(computer_score))

    wager = 'n'

    # ask to play again
    again = input("Type no to leave, enter to continue")
    if again == "no":
        break