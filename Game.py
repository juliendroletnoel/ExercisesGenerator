import json as j
import random
from Exercise import ExerciseList
from Player.Player_Controller import PlayerController
from Configuration import *
from pydub import AudioSegment

class Game:
    def __init__(self):
        """ Game initilization """

        # Ajouter configuration
        # 1) Nombre exercises
        # 2) Ratio Muscular
        # 3) Ratio Cardio
        # 4) Ratio Balance
        self.__exercises = ExerciseList()
        self.e = ExerciseList()

    def start_game(self):

        choice = -1
        while choice != 0:
            print ('1- Puiser de l''eau')
            print ('2- Amasser de la nourriture')
            print ('3- Construire un abris ')
            print ('4- Construire un radeau')
            print ('0- Quitter')
            
            choice = int(input('Votre choix'))
            print ()

            if choice == 1:
                print ('Puiser de l''eau')
                choices = self.__exercises.get_exercises_based_on_exercise_type_name('muscular')
                print()

                for i in range(1, 4):
                    print ('{}- {}'.format(i, choices[i-1].exercise_name))
                print()

                e = int(input('Votre Choix'))

            if choice == 2:
                print ('2 Amasser de la nourriture')
                choices = self.__exercises.get_exercises_based_on_body_part('legs')
                print()

                for i in range(1, 4):
                    print ('{}- {}'.format(i, choices[i-1].exercise_name))
                print()

                e = int(input('Votre Choix'))

            if choice == 3:
                print ('3 Construire un abris')
                choices = self.__exercises.get_exercises_based_on_exercise_type_name('cardio')            
                print()

                for i in range(1, 4):
                    print ('{}- {}'.format(i, choices[i-1].exercise_name))
                print()

                e = int(input('Votre Choix'))

g = Game()
g.start_game()