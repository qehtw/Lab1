import os

def read_input(file_name):
    """
    This function reads info from a CSV file.
    """
    input_info = []
    cur_path = os.path.dirname(__file__)
    resources_dir = os.path.join(cur_path, "..", "test", "resources")
    file_path = os.path.join(resources_dir, file_name)

    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(',')
            input_info.append(values)

    return input_info

def min_length(information):
    """
    This function makes few moves:
    1.Sort connections by values 
    2.Checks if all wells connected
    3.If some wells don`t connected it returns -1 
    4.Calculates minimal length
    """
    information.sort(key=lambda x: int(x[2]))
    visited = []
    length = 0
    for i in range(len(information)):
        cheked_wells = [information[i][0] , information[i][1]]
        if cheked_wells in visited:
            continue
        else:
            if cheked_wells[0] in visited or cheked_wells[1] in visited or visited == []:
                visited.append(information[i][0])
                visited.append(information[i][1])
                length += int(information[i][2])
            else:
                return -1
    if visited == []:
        return -1
    return length



def calculate_minimal_length(file_name):
    """
    This function activates all code 
    """
    information = read_input(file_name)
    print(information)
    result = min_length(information)
    return result



print(calculate_minimal_length('communication_wells.csv'))