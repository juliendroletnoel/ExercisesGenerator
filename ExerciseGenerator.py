import random
from Configuration import *
from ExerciseConfig import ExerciseConfig
from math import floor

class ExerciseGenerator(object):

    def __init__(self):
        ''' Builds a list of exercises based on configuration '''
        
        self.__exercises = []

        for json_exercise in exercises_list:

            exercise_type = json_exercise[0]
            exercise_body_part = json_exercise[1]
            exercise_name = json_exercise[2]

            # if exercise is already added, pass
            if exercise_name in [e.exercise_name for e in self.__exercises]:
                continue
            
            exercise_time_config = [e for e in exercises_config_list if e.exercise_config_name == exercise_type][0]
            exercise = Exercise(exercise_type, exercise_body_part, exercise_name, exercise_time_config)
            self.__exercises.append(exercise)

    def get_exercises_based_on_body_part(self, body_part_name):
        body_part_name = body_part_name.lower()

        exercises_based_on_body_part = [exercise for exercise in self.__exercises \
                                        if exercise.body_part_name == body_part_name]

        if len(exercises_based_on_body_part) == 0:
            raise ValueError(body_part_name)

        returned_exercises = []
        used_indexes = []
        while len(returned_exercises) < 3 and len(used_indexes) < len(exercises_based_on_body_part):
            random_index = random.randint(0, len(exercises_based_on_body_part)-1)
            if random_index in used_indexes:
                continue

            used_indexes.append(random_index)
            returned_exercises.append(exercises_based_on_body_part[random_index])

        return returned_exercises

    def get_exercises_based_on_exercise_type_name(self, exercise_type_name):
        exercise_type_name = exercise_type_name.lower()
    
        exercises_based_on_type = [exercise for exercise in self.__exercises \
                                   if exercise.exercise_type_name == exercise_type_name]

        if len(exercises_based_on_type) == 0:
            raise ValueError(exercise_type_name)

        returned_exercises = []
        used_indexes = []
        while len(returned_exercises) < 3 and len(used_indexes) < len(exercises_based_on_type):
            random_index = random.randint(0, len(exercises_based_on_type)-1)
            if random_index in used_indexes:
                continue

            used_indexes.append(random_index)
            returned_exercises.append(exercises_based_on_type[random_index])

        return returned_exercises

    def get_exercises_based_on_body_part_and_type(self, exercise_type_name, body_part_name):
        exercise_type_name = exercise_type_name.lower()
        body_part_name = body_part_name.lower()

        exercises_based_filter = [exercise for exercise in self.__exercises \
                                  if exercise.exercise_type_name == exercise_type_name \
                                      if exercise.body_part_name == body_part_name] 

        returned_exercises = []
        used_indexes = []
        while len(returned_exercises) < 3 and len(used_indexes) < len(exercises_based_filter):
            random_index = random.randint(0, len(exercises_based_filter)-1)
            if random_index in used_indexes:
                continue

            used_indexes.append(random_index)
            returned_exercises.append(exercises_based_filter[random_index])

        return returned_exercises

class Exercise(object):
    def __init__(self, exercise_type_name, body_part_name, exercise_name, exercise_config):

        if not isinstance(exercise_config, ExerciseConfig):
            raise TypeError(exercise_config)

        self.exercise_type_name = exercise_type_name
        self.exercise_config = exercise_config
        self.body_part_name = str(body_part_name).strip().lower()
        self.exercise_name = str(exercise_name).strip().lower()

    def get_exercise_time_in_seconds(self):
        return self.exercise_config.exercise_time_in_second

    def get_recovery_time_in_seconds(self):
        return self.exercise_config.recovery_time_in_second