from Exercises.ExerciseTimeConfig import ExerciseTimeConfig

class Exercise(object):
    def __init__(self, exercise_type_name, exercise_time_config, body_part_name, exercise_name):

        if not isinstance(exercise_time_config, ExerciseTimeConfig):
            raise TypeError(exercise_time_config)

        self.__exercise_type_name = exercise_type_name
        self.__body_part_name = body_part_name
        self.__exercise_name = exercise_name
        self.__exercise_time_config = exercise_time_config

    def get_exercise_time_in_seconds(self):
        return self.__exercise_time_config.exercise_time_in_second

    def get_recovery_time_in_seconds(self):
        return self.__exercise_time_config.recovery_time_in_second

    def get_displayable_exercise(self):
        return "{} ({})".format(self.__exercise_name, self.__body_part_name)

    def is_same_exercise_type(self, exercise_type_name):
        exercise_type_name = exercise_type_name.strip().lower()
        return self.__exercise_type_name == exercise_type_name

    def is_same_body_part_name(self, body_part_name):
        body_part_name = body_part_name.strip().lower()
        return self.__body_part_name == body_part_name