import random
from time import sleep
rps = ("rock", "paper", "scissors") #tuple of the possible inputs for the player.
yes = ("YES","Y", "y", "yes") #tuple for all the possible ways to say yes or no when asked to.
no = ("NO", "no", "n", "N")



def main_func(): 
    com_wins = 0 
    player_wins = 0
    player_remaining_wins = 3 - player_wins
    com_remaining_wins = 3 - com_wins
    while True: #Game Loop starts here.
        player = input("Rock,Paper or Scissors?\n>")
        computer = random.choice(rps)#Makes random choice out of the previous rps variable.
        print(computer)
        if player == computer:
            print("Tie. COM needs {} more wins to win while Player needs {} more wins to win!!".format(com_remaining_wins, player_remaining_wins))
            continue
        elif player == "paper" and computer == "rock":
            player_wins += 1
            player_wins
            player_remaining_wins = 3 - player_wins #defines how the variable is calculated.
            if player_remaining_wins == 0:
                print("Player won!!!")
                com_wins = 0
                player_wins = 0
                player_remaining_wins = 3 - player_wins
                com_remaining_wins = 3 - com_wins
            else:
                print("Player won and now has {} wins!! {} more to win".format(player_wins, player_remaining_wins))
                continue
        elif player == "rock" and computer == "scissors":
            player_wins += 1
            player_wins
            player_remaining_wins = 3 - player_wins
            if player_remaining_wins == 0:
                print("Player won!!!")
                com_wins = 0
                player_wins = 0
                player_remaining_wins = 3 - player_wins
                com_remaining_wins = 3 - com_wins
            else:
                print("Player won and now has {} wins!! {} more to win".format(player_wins, player_remaining_wins))
                continue
        elif player == "scissors" and computer == "paper":
            player_wins += 1
            player_wins
            player_remaining_wins = 3 - player_wins
            if player_remaining_wins == 0:
                print("Player won!!!")
                com_wins = 0
                player_wins = 0
                player_remaining_wins = 3 - player_wins
                com_remaining_wins = 3 - com_wins      
            else:
                print("Player won and now has {} wins!! {} more to win".format(player_wins, player_remaining_wins))
                continue
        elif computer == "paper" and player == "rock":
            com_wins += 1
            com_wins
            com_remaining_wins = 3 - com_wins
            if com_remaining_wins == 0:
                print("COM won!!!")
                com_wins = 0
                player_wins = 0
                player_remaining_wins = 3 - player_wins
                com_remaining_wins = 3 - com_wins
                
            else:
                print("COM won and now has {} wins!! {} more to win".format(com_wins, com_remaining_wins))
                continue
        elif computer == "rock" and player == "scissors":
            com_wins
            com_wins += 1
            com_remaining_wins = 3 - com_wins
            if com_remaining_wins == 0:
                print("COM won!!!")
                com_wins = 0
                player_wins = 0
                player_remaining_wins = 3 - player_wins
                com_remaining_wins = 3 - com_wins
                
            else:
                print("COM won and now has {} wins!! {} more to win".format(com_wins, com_remaining_wins))
                continue

        elif computer == "scissors" and player == "paper":
            com_wins
            com_wins += 1
            com_remaining_wins = 3 - com_wins
            if com_remaining_wins == 0:
                print("COM won!!!")
                com_wins = 0
                player_wins = 0
                player_remaining_wins = 3 - player_wins
                com_remaining_wins = 3 - com_wins
                
            else:
                print("COM won and now has {} wins!! {} more to win".format(com_wins, com_remaining_wins))
                continue
        else:
            print("I dont think you have the facilities for that big man")
            answer_3 = str(input("Do you want to play again?[y/n]\n>"))
            if answer_3 in yes:
                continue
            elif answer_3 in no:
                quit()
                sleep(2)
        answer2 = input("Do you want to play again?[y/n]")
        if answer2 in yes:
            continue
        else:
            sleep(2)
            quit()    

main_func()