class DifficultyConfiguration(object):

    def __init__(self, difficulty_name, repetitions_per_round, item_number_per_round):

        """
            Difficulty Level
            
            Challenge difficulty levels
            Defines how much exercise repetitions needed to complete a 'round' of exercise
            Defines how many item gained per 'round' completed

            example:
            - repetitions_per_round = 10
            - item_number_per_round = 4

            user does 60 reps
            60 / 10 = 6
            6 * 4 = 24 items gained
        """
        
        if not isinstance(difficulty_name, str):
            raise TypeError(difficulty_name)

        if not isinstance(repetitions_per_round, int):
            raise TypeError(repetitions_per_round)

        if not isinstance(item_number_per_round, int):
            raise TypeError(item_number_per_round)

        if repetitions_per_round < 0:
            raise ValueError(repetitions_per_round)

        if item_number_per_round < 0:
            raise ValueError(item_number_per_round)

        self.__difficulty_name = difficulty_name.lower()
        self.__repetitions_per_round = repetitions_per_round
        self.__item_number_per_round = item_number_per_round

    def get_difficulty_name(self):
        return self.__difficulty_name

    def get_repetitions_per_round(self):
        return self.__repetitions_per_round

    def get_item_number_per_round(self):
        return self.__item_number_per_round