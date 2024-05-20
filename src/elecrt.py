import os
import math


def read_input(file_name):
    """
    This function reads info from a txt file.
    """
    input_info = []
    cur_path = os.path.dirname(__file__)
    resources_dir = os.path.join(cur_path, "..", "test", "resources")
    file_path = os.path.join(resources_dir, file_name)

    with open(file_path, "r") as file:
        for line in file:
            values = list(map(int, line.strip().split(" ")))    
            input_info.append(values)

    return input_info


def data_check(distance, pillars):
    """
    This function checks if the data is true to the terms
    """

    if distance > 100 or distance < 1 or len(pillars) > 50:
        return False
    for i in range(0, len(pillars)):
        if pillars[i] > 100 or pillars[i] < 1:
            print(pillars[i])
            return False


def check_closer(next_heigth, current_heigth):

    target = 1

    if abs(current_heigth - next_heigth) < abs(current_heigth - target):
        return 1


def calculate_worst_scenario(pillars, distance):
    """
    This function creates worst possible heights of pillars
    """

    heights = len(pillars)

    value_bottom = 0
    value_top = 0

    for pillar in range(1, heights):
        
        previous_bottom_to_current_bottom = value_bottom + math.sqrt(distance ** 2 + (1 -1) ** 2)
        preevious_top_to_current_bottom = value_top + math.sqrt(distance ** 2 + (1 - pillars[pillar-1]) ** 2)
        current_value_bottom = max(previous_bottom_to_current_bottom, preevious_top_to_current_bottom)
        
        previous_bottom_to_current_top = value_bottom + math.sqrt(distance ** 2 + (pillars[pillar] - 1) ** 2)
        previous_top_to_current_top = value_top + math.sqrt(distance ** 2 + (pillars[pillar] - pillars[pillar - 1]) ** 2)
        current_value_top = max(previous_bottom_to_current_top, previous_top_to_current_top)

        value_bottom = current_value_bottom
        value_top = current_value_top

    wire_lenght = round(max(value_top, value_bottom), 2)

    return wire_lenght



def start_code(file_name):
    """
    This function start code
    """

    data_from_file = read_input(file_name)
    distance = data_from_file[0][0]
    pillars = data_from_file[1]
    if data_check(distance, pillars) == False:
        return False
    new_pillars = calculate_worst_scenario(pillars ,distance)
    return new_pillars


print( start_code('electr_input.txt'))