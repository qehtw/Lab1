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
    i = 0
    new_heigths_of_pillars = pillars
    total_length = 0
    for i in range(0, len(pillars) - 1):
        if new_heigths_of_pillars[i] > new_heigths_of_pillars[i + 1]:
            new_heigths_of_pillars[i + 1] = 1
            length = math.sqrt((new_heigths_of_pillars[i] - new_heigths_of_pillars[i + 1]) ** 2 + distance**2)
            total_length += length
            continue

        if new_heigths_of_pillars[i] == 1:
            length = math.sqrt((new_heigths_of_pillars[i] - new_heigths_of_pillars[i + 1]) ** 2 + distance**2)
            total_length += length
            continue

        if check_closer(new_heigths_of_pillars[i + 1], new_heigths_of_pillars[i]) == 1:
            new_heigths_of_pillars[i + 1] = 1
            length = math.sqrt((new_heigths_of_pillars[i] - new_heigths_of_pillars[i + 1]) ** 2 + distance**2)
            total_length += length
            continue

    return round(total_length,2)


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
