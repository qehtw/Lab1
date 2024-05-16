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

def is_closer_to(current_pillar_heigth , next_pillar_heigth):

    diff1 = abs(current_pillar_heigth - 1)
    diff2 = abs(current_pillar_heigth - next_pillar_heigth)

    if diff1 < diff2:
        return 1
    else: 
        if diff2 < diff1:
            return next_pillar_heigth
        else: 
            return False



def data_check(distance, pillars):

    """
    This function checks if the data is true to the terms
    """

    if distance > 100 or distance < 1 or len(pillars) > 50 :
        return False
    for i in range(0, len(pillars)):
        if pillars[i] > 100 or pillars[i] < 1:
            print(pillars[i])
            return False

def find_length_of_cabel(distance,pillars):
    
    """
    This function calculates lengths of cabel that we might need
    """

    total_length = 0
    number_of_pillars = len(pillars)
    current_pillar_heigth = pillars[0]
    next_pillar_heigth = pillars[1]
    for i in range(0,number_of_pillars-1):
        if is_closer_to(current_pillar_heigth , next_pillar_heigth) == next_pillar_heigth or next_pillar_heigth == current_pillar_heigth :
            next_pillar_heigth = 1
            length = math.sqrt((current_pillar_heigth - next_pillar_heigth )**2 + distance**2)
            current_pillar_heigth = 1
            next_pillar_heigth = pillars[i]
            total_length += length
        else:
            if current_pillar_heigth == 1 or is_closer_to(current_pillar_heigth, next_pillar_heigth) == 1:
                length = math.sqrt((current_pillar_heigth - next_pillar_heigth )**2 + distance**2)
                current_pillar_heigth = next_pillar_heigth
                next_pillar_heigth = pillars[i+1]
                total_length += length
            else:
                return 2
    return round(total_length , 2)

def start_code(file_name):
    
    """
    This function start code
    """

    data_from_file = read_input(file_name)
    distance = data_from_file[0][0]
    pillars = data_from_file[1]
    if data_check(distance, pillars) == False:
        return False
    return find_length_of_cabel(distance, pillars)
