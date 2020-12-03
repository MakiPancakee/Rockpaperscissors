#Importation for random
import random
from function import *

#Variable keep_playing (will serve in the final loop, when the player will choose to keep playing or not)
keep_playing = True
#Variable initialized to 0, will be incremented later    
points_pc = 0 
points = 0 

#Variables for the signs of the game
list_signs = ["Rock", "Paper" ,"Scissors"]

#while keep_playing is true, the loop will go on.
while True:
    #Pick sign
    pc_sign = random.choice(list_signs)

    #Call function for the player_sign
    player_sign = ask_player()

    #If tie
    if pc_sign == player_sign:
        points_pc += 1
        points += 1
        print(f"Pc choose {pc_sign}, this is AN EGALITYYY")

    #If win // ------------------------------------------------------ invalid syntax
    #elif ... :
    elif player_sign == "Paper" and pc_sign == "Rock":
        points += 2
    elif player_sign == "Rock" and pc_sign == "Scissors":
        points += 2
    elif player_sign == "Scissors" and pc_sign == "Paper":
        points += 2
    

    #If lose // ----------------------------------------------------- invalid syntax
    else:
        points_pc += 2
        print(f"Pc choose {pc_sign} you are born TOULOUSE")


    keep_playing = input(f"You have {points} points, the Pc has {points_pc} points. Want to keep playing ? (y/n)")
    #if y (for yes), that means True and the loop continue and repeat the cycle of the loop
    if keep_playing == "n":    
        print(f"Game is over ! Final score : Player : {points} / Pc : {points_pc}")
        break