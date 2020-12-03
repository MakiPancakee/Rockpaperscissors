def ask_player():
    #Player's choice, capitalize the first letter
    player_sign = input(f"Pliz, choose between Rock, Paper & Scissors: ")
    player_sign = player_sign.capitalize().strip(".")
    #strip, espace, point..
    return player_sign

#def match(pc_sign, player_sign, points):

    #message = f"Pc choose {pc_sign} you are the WINNER"
    #return message, points
