import random

rps = ("rock", "paper", "scissors")


computer = random.choice(rps)
yes = ("YES","Y", "y", "yes")
no = ("NO", "no", "n", "N")

def main_func():
    while True:
        computer = random.choice(rps)
        break
        
    player = input("Rock,Paper or Scissors?\n>")
    print(computer)
    while True:
        if player == computer:
            print("Tie")
            break
        elif player == "paper" and computer == "rock":
            print("Player won")
            break
        elif player == "rock" and computer == "scissors":
            print("Player won")
            break
        elif player == "scissors" and computer == "paper":
            print("Player won")
            break
        elif computer == "paper" and player == "rock":
            print("COM won") 
            break
        elif computer == "rock" and player == "scissors":
            print("COM won")
            break
        elif computer == "scissors" and player == "paper":
            print("COM won")
            break
        else:
            print("I dont think you have the facilities for that big man")
            answer_3 = str(input("Do you want to play again?[y/n]\n>"))
            if answer_3 in yes:
                main_func()
            elif answer_3 in no:
                quit()
            break
    answer_2 = str(input("Do you want to play again?[y/n]\n>"))
    if answer_2 in yes:
        main_func()
    elif answer_2 in no:
        quit()

main_func()







