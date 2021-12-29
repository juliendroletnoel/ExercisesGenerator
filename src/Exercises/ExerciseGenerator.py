from os import close
import random
import json
import os.path
from Exercises.Exercise import *
from Exercises.ExerciseTimeConfig import ExerciseTimeConfig
from Exercises.MuscularRange import MuscularRange

__EXERCISES_TYPES = ('muscular', 'cardio', 'balance')
__EXERCISES_DIFFICULTIES = ('beginner', 'intermediate', 'beast')

class ExerciseGenerator(object):

    def __init__(self):
        """ Loads exercises json file 
            Exercises.json -> contains exercises
            ExerciseTimeConfig.json -> contains exercise and recovery time
            MuscularRanges.json -> contains reps ranges for muscular exercises (bulk or lean muscles)

            loads Exercises in a list of exercises
        """

        ### Configuration file names ###
        __configuration_folder_name = 'Exercises/Configuration'
        __exercises_file_name = os.path.join(__configuration_folder_name, "Exercises.json")
        __exercises_time_config_file_name = os.path.join(__configuration_folder_name, "ExerciseTimeConfigs.json")
        __muscular_range_file_name = os.path.join(__configuration_folder_name, "MuscularRepetitionsRanges.json")

        # Exercises list (Exercise Type, Body Part, Exercise name)
        json_file = json.load(open(__exercises_file_name))

        m = json_file['muscular']
        muscular_exercises = ((body, exer) for body in m.keys() for exer in m[body])

        c = json_file['cardio']
        cardio_exercises = ((body, exer) for body in c.keys() for exer in c[body])

        b = json_file['balance']
        balance_exercises = ((body, exer) for body in b.keys() for exer in b[body])

        # Exercises time configuration list
        json_file = json.load(open(__exercises_time_config_file_name))
        json_exercise_config_list = [(key.lower(), [json_file[key][time] for time in json_file[key]]) for key in json_file.keys()]
        exercises_time_config_list = [ExerciseTimeConfig(name, ex_time, re_time) for name, (ex_time, re_time) in json_exercise_config_list]

        self.__exercises = []

        # Muscular execises creation
        exercise_time_config = [e for e in exercises_time_config_list if e.exercise_config_name == 'muscular'][0] 
        for body_part, exer in muscular_exercises:
            exercise = MuscularExercise(exercise_time_config, body_part, exer)
            self.__exercises.append(exercise)

        # Cardio exercises creation
        exercise_time_config = [e for e in exercises_time_config_list if e.exercise_config_name == 'cardio'][0] 
        for body_section, exer in cardio_exercises:
            exercise = CardioExercise(exercise_time_config, body_section, exer)
            self.__exercises.append(exercise)

        # Balance exercises
        exercise_time_config = [e for e in exercises_time_config_list if e.exercise_config_name == 'balance'][0] 
        for body_section, exer in balance_exercises:
            exercise = BalanceExercise(exercise_time_config, body_section, exer)
            self.__exercises.append(exercise)

        # Muscular Ranges - Not used yet
        json_file = json.load(open(__muscular_range_file_name))
        m = json_file['muscular_repetitions_ranges']
        __muscular_ranges = [((k,) + tuple(m[k].values())) for k in m]

        self.__muscular_range = MuscularRange()
        
        for name, min_reps, max_reps in __muscular_ranges:
            self.__muscular_range.add_muscular_range(name, min_reps, max_reps)
        ###################################

    def get_exercises_based_on_filter(self, exercise_type_name, body_part_name, nb_exercises=3):
        exercise_type_name = exercise_type_name.lower()
        body_part_name = body_part_name.lower()

        return self.__get_exercises(exercise_type_name, body_part_name, nb_exercises)
        
    def __get_exercises(self, exercise_type_name, body_part_name, nb_exercises):
        
        exercises_based_filter = [exercise for exercise in self.__exercises \
                                  if exercise.is_same_exercise_type(exercise_type_name)]

        if len(exercises_based_filter) == 0:
            raise ValueError(exercise_type_name)
            
        if len(body_part_name) > 0:
            exercises_based_filter = [exercise for exercise in self.__exercises \
                                        if exercise.is_same_body_part_name(body_part_name)]
        
        returned_exercises = []
        used_indexes = []
        while len(returned_exercises) < nb_exercises and len(used_indexes) < len(exercises_based_filter):
            random_index = random.randint(0, len(exercises_based_filter)-1)
            if random_index in used_indexes:
                continue

            used_indexes.append(random_index)
            returned_exercises.append(exercises_based_filter[random_index])

        return returned_exercises

