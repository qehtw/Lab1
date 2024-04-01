def Check_if_sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def find_start_pos(arr): 
    for i in range (0 ,len(arr)-1):
        if arr[i]    > arr[i+1]:
            return i  

def find_last_pos(arr):
    for i in range (len(arr)-1 , 0 , -1):
        if arr[i] < arr[i-1]:
            return i
        
def max_in_new_arr(subarray):
    new_max = max(subarray)
    return new_max

def min_in_new_arr(subarray):
    new_min = min(subarray)
    return new_min

def find_start_spot(arr ,new_min ,start_index ):
    while new_min < arr[start_index-1] and start_index > 0:
        start_index -= 1 
    return start_index

def find_end_spot(arr ,new_max ,end_index ):
    while new_max > arr[end_index+1] and end_index + 1 < len(arr):
        end_index += 1 
    return end_index


def finder(arr):
    start_pos = find_start_pos(arr)
    end_pos = find_last_pos(arr)
    subarray = arr[start_pos :end_pos + 1]
    if Check_if_sorted(arr) or len(arr) == 1:
        return (-1 , -1)
    else:
        new_max = max_in_new_arr(subarray)
        new_min = min_in_new_arr(subarray)
        print (find_start_spot(arr, new_min, start_pos), "," ,find_end_spot(arr, new_max, end_pos))


arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
finder(arr)
