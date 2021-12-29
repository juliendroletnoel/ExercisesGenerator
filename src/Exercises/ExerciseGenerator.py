from os import close
import random
import json
import os.path
from Exercises.Exercise import *
from Exercises.ExerciseTimeConfig import ExerciseTimeConfig
from Exercises.MuscularRange import MuscularRange

class ExerciseGenerator(object):

    def __init__(self):
        """ Loads exercises json file 
            Exercises.json -> contains exercises
            ExerciseTimeConfig.json -> contains exercise and recovery time
            MuscularRanges.json -> contains reps ranges for muscular exercises (bulk or lean muscles)

            loads Exercises in a list of exercises
        """

        # Instance variables
        self.__muscular_range = MuscularRange()
        self.__exercises = []
        self.__available_exercises_types_name = []
        self.__available_body_parts_name = {}

        ### Configuration file names ###
        __configuration_folder_name = 'Exercises/Configuration'
        __exercises_file_name = os.path.join(__configuration_folder_name, "Exercises.json")
        __exercises_time_config_file_name = os.path.join(__configuration_folder_name, "ExerciseTimeConfigs.json")
        __muscular_range_file_name = os.path.join(__configuration_folder_name, "MuscularRepetitionsRanges.json")

        # Exercises type configuration
        json_file = json.load(open(__exercises_time_config_file_name))
        json_exercise_config_list = [(key.lower(), [json_file[key][time] for time in json_file[key]]) for key in json_file.keys()]
        exercises_time_config_list = [ExerciseTimeConfig(name, ex_time, re_time) for name, (ex_time, re_time) in json_exercise_config_list]

        # Exercises list (Exercise Type, Body Part, Exercise name)
        json_file = json.load(open(__exercises_file_name))
        self.__available_exercises_types_name = json_file.keys()

        for exercise_type_name in self.__available_exercises_types_name:
            m = json_file[exercise_type_name]
            exercises = ((body, exer) for body in m.keys() for exer in m[body])
            exercise_time_config = [e for e in exercises_time_config_list if e.exercise_config_name == exercise_type_name][0] 

            available_body_parts = []
      
            for body_part, exercise_name in exercises:
                exercise = Exercise(exercise_type_name, exercise_time_config, body_part, exercise_name)
                self.__exercises.append(exercise)

                available_body_parts.append(body_part)

            self.__available_body_parts_name[exercise_type_name] = available_body_parts

        # Muscular Ranges - Not used yet
        json_file = json.load(open(__muscular_range_file_name))
        m = json_file['muscular_repetitions_ranges']
        __muscular_ranges = [((k,) + tuple(m[k].values())) for k in m]
        
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
            exercises_based_filter = [exercise for exercise in exercises_based_filter \
                                        if exercise.is_same_body_part_name(body_part_name)]
        
        if (len(exercises_based_filter) == 0):
            raise ValueError(body_part_name)

        returned_exercises = []
        used_indexes = []
        while len(returned_exercises) < nb_exercises and len(used_indexes) < len(exercises_based_filter):
            random_index = random.randint(0, len(exercises_based_filter)-1)
            if random_index in used_indexes:
                continue

            used_indexes.append(random_index)
            returned_exercises.append(exercises_based_filter[random_index])

        return returned_exercises

    def get_available_exercise_types(self):
        """
            Provide a tuple containing the name of the available exercises type
        """
        return tuple(self.__available_exercises_types_name)

    def get_available_body_part_name(self, exercise_type_name):
        """
            Provide a tuple of the available body part name based on exercise type name
            Raise a ValueError if exercise_type_name is unknown
        """
        
        if not exercise_type_name in self.__available_exercises_types_name:
            raise ValueError("'{}' was given, but '{}' are only available".format( exercise_type_name,\
            ','.join(self.__available_exercises_types_name)))

        return tuple(self.__available_body_parts_name[exercise_type_name])