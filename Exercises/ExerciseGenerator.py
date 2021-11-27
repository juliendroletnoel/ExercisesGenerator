import random
import json
import os.path
from Exercises.Exercise import *
from Exercises.ExerciseTimeConfig import ExerciseTimeConfig

__EXERCISES_TYPES = ('muscular', 'cardio', 'balance')
__EXERCISES_DIFFICULTIES = ('beginner', 'intermediate', 'beast')

class ExerciseGenerator(object):

    def __init__(self):
        """ Loads exercises json file 
            Exercises.json -> contains exercises
            ExerciseTimeConfig.json -> contains exercise and recovery time
            MuscularConfigs.json -> contains reps ranges for muscular exercises (bulk or lean muscles)

            loads Exercises in a list of exercises
        """

        ### Configuration file names ###
        __configuration_folder_name = 'Exercises/Configuration'
        __exercises_file_name = os.path.join(__configuration_folder_name, "Exercises.json")
        __exercises_time_config_file_name = os.path.join(__configuration_folder_name, "ExerciseTimeConfigs.json")
        __muscular_config_name = os.path.join(__configuration_folder_name, "MuscularConfigs.json")

        # Exercises list (Exercise Type, Body Part, Exercise name)
        j2 = json.load(open(__exercises_file_name))
        muscular_exercises = [(diff, body, exer) for diff in j2['muscular'].keys() for body in j2['muscular'][diff].keys() for exer in j2['muscular'][diff][body]]
        cardio_exercises = [(diff, body, exer) for diff in j2['cardio'].keys() for body in j2['cardio'][diff].keys() for exer in j2['cardio'][diff][body]]
        balance_exercises = [(diff, body) for diff in j2['balance'].keys() for body in j2['balance'][diff]]

        # Exercises time configuration list
        j = json.load(open(__exercises_time_config_file_name))
        json_exercise_config_list = [(key.lower(), [j[key][time] for time in j[key]]) for key in j.keys()]
        exercises_time_config_list = [ExerciseTimeConfig(name, ex_time, re_time) for name, (ex_time, re_time) in json_exercise_config_list]

        self.__exercises = []

        # Muscular execises creation
        for diff, body, exer in muscular_exercises:
            exercise_time_config = [e for e in exercises_time_config_list if e.exercise_config_name == 'muscular'][0]    
            exercise = MuscularExercise('muscular', diff, exercise_time_config, body, exer)
            self.__exercises.append(exercise)

        # Cardio exercises creation
        for diff, body_section, exer in cardio_exercises:
            exercise_time_config = [e for e in exercises_time_config_list if e.exercise_config_name == 'cardio'][0]    
            exercise = CardioExercise('cardio', diff, exercise_time_config, body_section, exer)
            self.__exercises.append(exercise)

        # Balance exercises
        for diff, exer in balance_exercises:
            exercise_time_config = [e for e in exercises_time_config_list if e.exercise_config_name == 'balance'][0]    
            exercise = BalanceExercise('balance', diff, exercise_time_config, exer)
            self.__exercises.append(exercise)

    def get_exercises_based_on_filter(self, difficulty, exercise_type_name, body_part_name, nb_exercises=3):
        exercise_type_name = exercise_type_name.lower()
        body_part_name = body_part_name.lower()

        return self.__get_exercises(difficulty, exercise_type_name, body_part_name, nb_exercises)
        
    def __get_exercises(self, difficulty, exercise_type_name, body_part_name, nb_exercises):
        
        exercises_based_filter = [exercise for exercise in self.__exercises \
                                  if exercise.exercise_type_name == exercise_type_name \
                                      if exercise.difficulty_name == difficulty]

        if len(exercises_based_filter) == 0:
            raise ValueError(exercise_type_name)
            
        if len(body_part_name) > 0:
            exercises_based_filter = [exercise for exercise in self.__exercises \
                                        if exercise.body_part_name == body_part_name]
        
        returned_exercises = []
        used_indexes = []
        while len(returned_exercises) < nb_exercises and len(used_indexes) < len(exercises_based_filter):
            random_index = random.randint(0, len(exercises_based_filter)-1)
            if random_index in used_indexes:
                continue

            used_indexes.append(random_index)
            returned_exercises.append(exercises_based_filter[random_index])

        return returned_exercises

