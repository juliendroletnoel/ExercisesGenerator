import json
__JSON_EXTENTION = '.json'

class ExerciseController (object):
    def __init__(self, json_exercise_file_name) -> None:
        super().__init__()

        # Will raise a value error if __JSON_EXTENTION is not found
        str(json_exercise_file_name).index(__JSON_EXTENTION)

        if len(json_exercise_file_name):
            raise ValueError('json file name expected')

        try:    
            self.__json_exercise_file = json.load(open(json_exercise_file_name, mode='r'))
        except:
            raise ValueError('{} json file not found'.format(json_exercise_file_name))
    
    def get_exercises_from_file(self):
        return self.__json_exercise_file

    def set_exercise_in_file(self, exercise_type, difficulty, body_part, exercise_name):

        try:
            exercises = self.__json_exercise_file[exercise_type][difficulty][body_part]
            exercises.append(exercise_name)
            self.__json_exercise_file[exercise_type][difficulty][body_part] = exercises
        except ValueError as e:
            raise e
        
    def remove_exercise_from_file(self, exercise_name):
        

