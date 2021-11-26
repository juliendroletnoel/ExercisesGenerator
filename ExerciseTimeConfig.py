class ExerciseTimeConfig(object):
    def __init__(self, exercise_config_name, exercise_time_in_second, recovery_time_in_second):
        
        try:
            self.exercise_config_name = exercise_config_name
            self.exercise_time_in_second = int(exercise_time_in_second)
            self.recovery_time_in_second = int(recovery_time_in_second)
        except TypeError as e:
            raise e
        
        if self.exercise_time_in_second <= 0:
            raise ValueError(self.exercise_time_in_second)

        if self.recovery_time_in_second > self.exercise_time_in_second:
            raise ValueError(self.recovery_time_in_second)

        
