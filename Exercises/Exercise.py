from Exercises.ExerciseTimeConfig import ExerciseTimeConfig

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
        self.body_part_name = ''
        self.exercise_name = str(balance_pose_name).strip().lower()