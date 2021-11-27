from Challenges.ChallengeGenerator import ChallengeGenerator
from pydub import AudioSegment

from ItemType import Food, Water

class Game:
    def __init__(self):
        """ Game initilization """

        # Ajouter configuration
        # 1) Nombre exercises
        # 2) Ratio Muscular
        # 3) Ratio Cardio
        # 4) Ratio Balance
        self.__challenge_generator = ChallengeGenerator()

    def start_game(self):

        choice = -1
        while choice != 0:
            print ()
            print ('1- Puiser de l''eau')
            print ('2- Amasser de la nourriture')
            print ('3- Construire un abris ')
            print ('4- Construire un radeau')
            print ('0- Quitter')
            print ()

            choice = int(input('Votre choix : '))
            print ()

            if choice == 1:
                print ('Puiser de l''eau')
                choices = self.__challenge_generator.generate_resources_challenges(3, Water, 'beast', 'chest', 'muscular')
                print()

                for i in range(1, 4):
                    print ('{} - {}'.format(i, choices[i-1].get_displayed_challenge()))
                print()

                e = int(input('Votre Choix : '))

                choices[e-1].display_and_start_challenge()

            if choice == 2:
                print ('2 Amasser de la nourriture')
                choices = self.__challenge_generator.generate_resources_challenges(3, Food, 'beginner', '', 'cardio')
                print()

                for i in range(1, 4):
                    print ('{} - {}'.format(i, choices[i-1].get_displayed_challenge()))
                print()

                e = int(input('Votre Choix : '))

                choices[e-1].display_and_start_challenge()

            if choice == 3:
                print ('3 Construire un abris')
                choices = self.__challenge_generator.generate_resources_challenges(3, Water, 'beast', '', 'balance')
                print()

                for i in range(1, 4):
                    print ('{} - {}'.format(i, choices[i-1].get_displayed_challenge()))
                print()

                e = int(input('Votre Choix : '))

                choices[e-1].display_and_start_challenge()

g = Game()
g.start_game()