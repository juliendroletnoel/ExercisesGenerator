from Bag import Bag
from Challenges.DifficultyConfiguration import DifficultyConfiguration
from ItemType import ItemType
from Item import Item
from time import sleep
from math import floor
from Exercises.ExerciseGenerator import ExerciseGenerator
from Challenges import difficulty_configurations

class ChallengeGenerator(object):
    def __init__(self):
        self.__exercise_generator = ExerciseGenerator()
        self.__difficulty_configurations = [DifficultyConfiguration(e[0], e[1], e[2]) for e in difficulty_configurations]

    def generate_resources_challenges(self, nb_exercise, gained_item_type, difficulty_name, body_part, exercise_type_name):
        """
            Build list of resource challenges based

            - Number of exercises
            - Gained_item_type (resource gained)
            - Difficulty level
        """

        if len(exercise_type_name) == 0:
            raise ValueError('An exercise type name must be defined to create resources challenges')

        if not issubclass(gained_item_type, ItemType):
            raise TypeError(gained_item_type)

        exercises = []
        challenges = []
        difficulty_name = difficulty_name.lower()
        difficulty_config = [config for config in self.__difficulty_configurations if config.get_difficulty_name() == difficulty_name]

        if len(difficulty_config) == 0:
            raise ValueError('[{}] expected, "{}" was given'.format(self.__difficulty_configurations, difficulty_name))

        difficulty_config = difficulty_config[0]
        exercises = self.__exercise_generator.get_exercises_based_on_filter(difficulty_name, \
                                                                            exercise_type_name, \
                                                                            body_part, \
                                                                            nb_exercise)
        
        reps_per_round = difficulty_config.get_repetitions_per_round()
        item_per_round = difficulty_config.get_item_number_per_round()

        challenges = [ResourceChallenge(exercise, gained_item_type, reps_per_round, item_per_round) for exercise in exercises]

        return challenges

class BuildingChallenge(object):
    def __init__(self, player_bag, needed_items, built_item):
        """
            BuildingChallenge: Gain a special item against resources
        """

        if not isinstance(needed_items, []):
            raise TypeError(needed_items)

        if len(needed_items) == 0:
            raise ValueError(needed_items)

        if any(not isinstance(item, Item) for item in needed_items):
            raise TypeError("array do not contains items")

        if not isinstance(player_bag, Bag):
            raise (player_bag)

        if not isinstance(built_item, Item):
            raise TypeError(built_item)

        self.__needed_items = needed_items
        self.__bag = player_bag
        self.__built_item = built_item

    def get_item_against_resource(self):
        """
            Returned the built item if needed resources are available in player's bag
            None otherwise

            Remove resources from bag if all resources were available
        """
        for needed_item in self.__needed_items:
            item = self.__bag.get_item_by_item_type(needed_item.item_type)
            if item is None:
                return None
            if item.quantity < needed_item.quantity:
                return None

            self.__bag.remove_item_from_bag(item)

        return self.__built_item

class ResourceChallenge(object):
    def __init__(self, exercise, item_type, reps_per_round, quantity_item_returned_per_reps):
        """
            RessourcerChallenge: Perform an exercise to gain resources (water, food, ect)

            - define an exercise to obtain the item type (water, food, ect)
            - item quantity is defined by number of reps done by user (in defined time)
              divied by reps_for_item and multiplied by quantity_item_returned_per_reps
        """

        if not issubclass(item_type, ItemType):
            raise TypeError(item_type)

        if not isinstance(reps_per_round, int):
            raise TypeError(reps_per_round)

        if not isinstance(quantity_item_returned_per_reps, int):
            raise TypeError(quantity_item_returned_per_reps)

        if reps_per_round < 0:
            raise ValueError(reps_per_round)

        if quantity_item_returned_per_reps < 0:
            raise ValueError(quantity_item_returned_per_reps)

        self.__exercise = exercise
        self.__item_type = item_type
        self.__item_type_name = item_type.__name__
        self.__reps_per_round = reps_per_round
        self.__items_per_round = quantity_item_returned_per_reps
    
    def get_displayed_challenge(self):
        return '{}: {} part of {} gained per {} round'.format(self.__exercise.exercise_name, \
                            self.__items_per_round, self.__item_type_name, self.__reps_per_round)

    def get_exercise_name(self):
        return self.__exercise.exercise_name

    def display_and_start_challenge(self):
        
        """
            Display and run the exercise
            Return the number of items based on the number of repetitions
        """
        recovery_time = self.__exercise.get_recovery_time_in_seconds()
        exercise_time = self.__exercise.get_exercise_time_in_seconds()

        print('= Exercise {} ='.format(self.__exercise.exercise_name))
        print()
        print('= {} units of {} gained by {} reps completed ='.format(self.__items_per_round, \
                                                                        self.__item_type_name, \
                                                                        self.__reps_per_round))
        print()
        print('= {} seconds to complete exercise ='.format(exercise_time))
        print('= {} seconds to prepare = '.format(recovery_time))
        print()
        sleep(recovery_time-3)
        print('=== Starting exercise ===')
        print()

        for i in range(3, 0, -1):
            print(i, ' ', end='')
            sleep(1)
        
        print('== GO ==')
        print()

        for i in range(0, exercise_time):
            print('. ', end="")
            sleep(1)

        print()
        print("== STOP ==")
        nb_repetitions = ''
        while not isinstance(nb_repetitions, int):
            try:
                nb_repetitions = int(input("Number of repetitions performed : "))
            except:
                pass

        item_quantity = floor(nb_repetitions / self.__reps_per_round) * self.__items_per_round

        if item_quantity > 0:
            item = Item(self.__item_type, item_quantity)
        else:
            print ('== Not enough repetitions to gather {} ... ==='.format(self.__item_type.__name__))
            return None

        print("== Congratulations ==")
        print()
        print("{} units of {} were gained".format(item_quantity, item.item_type))
        input('OK ! <enter to continue>')

        return item
    
    def run_exercise_based_on_time(self):
        pass