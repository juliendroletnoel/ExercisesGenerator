import math as m
from time import sleep
import random
from Configuration import *
from Exercise import build_exercise
from playsound import playsound

def build_challenge(challenge):
    
    title = challenge["title"]
    description = challenge["description"]
    exercises_list = [exercises for exercises in challenge['exercises']]

    exercises = [build_exercise(exercise['description'], exercise['exercise'][0], exercise['exercise'][1]) for exercise in exercises_list]
    
    return Challenge(title, description, exercises)

class Challenge(object):

    weight_in_lbs = default_weight_in_lbs
    repetitions = default_repetitions
    difficulty = 1.00
    time_in_seconds = default_time_in_second
        
    def __init__(self, title, description, exercises):
    
        self.__title = title
        self.__description = description
        self.__exercises = exercises

        random.seed(random_seed)

    def display_and_start_exercice(self):
        nb_exercises = len(self.__exercises)
        valid_choice = False

        print (self.__title)
        for text in self.__description :
            print (text)

        for exercise in self.__exercises:
            exercise.display_exercise_description()

        while not valid_choice is True:
            choice = int(input("Votre choix : "))
            choice = int(choice) - 1
            if choice >= 0 and choice < nb_exercises:
                valid_choice = True

        chosen_exercise = self.__exercises[choice]
        chosen_exercise.display_exercise()
        self.display_challenge(chosen_exercise)
        self.start_challenge()

        return chosen_exercise

    def display_challenge(self, chosen_exercise):
        
        exercise_type = chosen_exercise.get_exercise_type()
        
        if exercise_type == 'strength':
            print ('Poids (lbs) : {}'.format(Challenge.weight_in_lbs))
            pass
        elif exercise_type in ('strength', 'cardio'):
            print ('Nombre de repetition : {}'.format(Challenge.repetitions))
            pass
        elif exercise_type == 'balance':
            print('Temps de la pose : {}'.format(Challenge.time_in_seconds))
            pass

    def start_challenge(self):
        print ('STARTING CHALLENGE')
                
        #self.display_challenge()
        #self.__play_music()

        key_point = 15
        key_stone = m.floor(Challenge.time_in_seconds/key_point)
        print (key_point*'* ', Challenge.time_in_seconds, 'seconds')
        for second in range(0, Challenge.time_in_seconds):
            sleep(1)
            if second % key_stone == 0:
                print ('= ', end='', flush=True)

        print ('Time is up!')