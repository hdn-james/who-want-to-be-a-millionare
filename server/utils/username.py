import configuration
from server.models.player import Player

def checkUsername(name: str):
    check = True
    #check valid string
    if len(name) > 10:
        check = False
        return "Username is not longer than 10 characters. \nPlease choose another one"
    else:
        for char in name:
            if not char.isalpha() and not char.isdigit() and char != '_':
                check = False
                return "Username just includes [a-z, A-Z, 0-9, _]. \nPlease choose another one"
        
        if check:        
            #check distinct
            players = configuration.players
            for player in players:
                if player.username == name:
                    check = False
                    return "Username has been already registered. \nPlease choose another one"
            if check:
                player = Player(name)
                configuration.players.append(player)
                return None