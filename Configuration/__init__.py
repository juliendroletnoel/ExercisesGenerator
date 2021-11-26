import os.path
import json
import time
from ExerciseTimeConfig import ExerciseTimeConfig

print ('Configuration module initialization')

### Configuration file names ###
__configuration_folder_name = 'Configuration'
__exercises_file_name = os.path.join(__configuration_folder_name, "Exercises.json")
__exercises_time_config_file_name = os.path.join(__configuration_folder_name, "ExerciseTimeConfigs.json")
__muscular_config_name = os.path.join(__configuration_folder_name, "MuscularConfigs.json")
__music_folder_name = os.path.join('music')

### Json content loaded in arrays and dictionnaries ###

## List of challenge (Order of the challenge in the list is the same when displayed)

# Exercises list (Exercise Type, Body Part, Exercise name)
j2 = json.load(open(__exercises_file_name))
muscular_exercises = [(diff, body, exer) for diff in j2['muscular'].keys() for body in j2['muscular'][diff].keys() for exer in j2['muscular'][diff][body]]
cardio_exercises = [(diff, body, exer) for diff in j2['cardio'].keys() for body in j2['cardio'][diff].keys() for exer in j2['cardio'][diff][body]]
balance_exercises = [(diff, body) for diff in j2['balance'].keys() for body in j2['balance'][diff]]

# Exercises time configuration list
j = json.load(open(__exercises_time_config_file_name))
json_exercise_config_list = [(key.lower(), [j[key][time] for time in j[key]]) for key in j.keys()]
exercises_time_config_list = [ExerciseTimeConfig(name, ex_time, re_time) for name, (ex_time, re_time) in json_exercise_config_list]

 # File serialization actions
actions = ["new", "load"]
action_new = 0
action_load = 1

# Music file initialization
music_files = []

for root, dir, music_file_names in os.walk(__music_folder_name):
    
    if len(music_file_names) == 0:
        continue

    current_sub_folder = os.path.split(root)[-1]
    current_sub_folder = current_sub_folder.lower()
    if current_sub_folder in ('muscular', 'cardio', 'balance'):
        music_tuple = (current_sub_folder, [os.path.join(root, music_file_name) for music_file_name in music_file_names])
        music_files.append(music_tuple)

# Randomizer initialization
random_seed = int(time.time()) % 100

