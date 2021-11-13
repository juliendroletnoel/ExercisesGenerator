# Player Controller
from Player.Player import Player

class PlayerController:

    def __init__(self):
        self.__player_list = []

    def define_players(self):

        print ("Definir les joueurs")
        print ()
        
        players_are_all_defined = False
        player_number = 1
        while not players_are_all_defined:
            print ('Entrer le joueur # {}'.format(player_number))
            print()
            player_name = input('Nom complet du joueur :')
            player_nickname = input('Surnom du joueur :')
            player_age = int(input('Age du joueur : '))
            confirm = int(input('Les informations entrees sont valides? (1=Oui, 0=Non) : '))

            if not confirm:
                continue

            player = Player(player_name, player_nickname, player_age, player_number)
            self.__player_list.append(player)

            player_number+=1
            
            players_are_all_defined = bool(input('Les joueurs sont tous definis? (1=Oui, 0=Non) :'))

    def get_player_list(self):
        return self.__player_list