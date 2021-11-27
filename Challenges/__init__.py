import os.path
import json
import time
from Challenges.DifficultyConfiguration import DifficultyConfiguration

"""
Challenges initialization
"""

### Configuration file names ###
__configuration_folder_name = 'Challenges'
__challenge_configuration_file_name = os.path.join(__configuration_folder_name, "ChallengeConfiguration.json")

json_object = json.load(open(__challenge_configuration_file_name, mode='r'))
__difficulty_list = [k['difficulty_name'] for k in json_object['difficulties']]
difficulty_configurations = [list(j.values()) for j in json_object['difficulties']]

def get_difficulty_list():
    return __difficulty_list