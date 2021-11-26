import random
from Configuration import *
from ExerciseTimeConfig import ExerciseTimeConfig
from math import floor

class ExerciseGenerator(object):

    def __init__(self):
        ''' Builds a list of exercises based on configuration '''
        
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
            exercise = BalanceExercise('Balance', diff, exercise_time_config, exer)
            self.__exercises.append(exercise)

    def get_exercises_based_on_exercise_type_name(self, exercise_type_name, nb_exercises=3):
        exercise_type_name = exercise_type_name.lower()
    
        exercises_based_on_type = [exercise for exercise in self.__exercises \
                                   if exercise.exercise_type_name == exercise_type_name]

        if len(exercises_based_on_type) == 0:
            raise ValueError(exercise_type_name)

        returned_exercises = []
        used_indexes = []
        while len(returned_exercises) < nb_exercises and len(used_indexes) < len(exercises_based_on_type):
            random_index = random.randint(0, len(exercises_based_on_type)-1)
            if random_index in used_indexes:
                continue

            used_indexes.append(random_index)
            returned_exercises.append(exercises_based_on_type[random_index])

        return returned_exercises

    def get_exercises_based_on_body_part_and_type(self, exercise_type_name, body_part_name, nb_exercises=3):
        exercise_type_name = exercise_type_name.lower()
        body_part_name = body_part_name.lower()

        exercises_based_filter = [exercise for exercise in self.__exercises \
                                  if exercise.exercise_type_name == exercise_type_name \
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

class Exercise(object):
    def __init__(self, exercise_type_name, difficulty, exercise_time_config):

        if not isinstance(exercise_time_config, ExerciseTimeConfig):
            raise TypeError(exercise_time_config)

        self.exercise_type_name = exercise_type_name
        self.__exercise_time_config = exercise_time_config
        self.difficulty_name = str(difficulty).strip().lower()

    def get_exercise_time_in_seconds(self):
        return self.__exercise_time_config.exercise_time_in_second

    def get_recovery_time_in_seconds(self):
        return self.__exercise_time_config.recovery_time_in_second

class MuscularExercise(Exercise):
    def __init__(self, exercise_type_name, difficulty, exercise_time_config, body_part_name, exercise_name):
        super().__init__(exercise_type_name, difficulty, exercise_time_config)
        self.body_part_name = str(body_part_name).strip().lower()
        self.exercise_name = str(exercise_name).strip().lower()

class CardioExercise(Exercise):
    def __init__(self, exercise_type_name, difficulty, exercise_time_config, body_section_name, exercise_name):
        super().__init__(exercise_type_name, difficulty, exercise_time_config)
        self.body_part_name = str(body_section_name).strip().lower()
        self.exercise_name = str(exercise_name).strip().lower()

class BalanceExercise(Exercise):
    def __init__(self, exercise_type_name, difficulty, exercise_time_config, balance_pose_name):
        super().__init__(exercise_type_name, difficulty, exercise_time_config)
        self.exercise_name = str(balance_pose_name).strip().lower()