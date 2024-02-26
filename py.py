def Check_if_sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def find_last_pos(arr):
    max_index = 0
    for i in range (0 ,len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            max_index = arr.index(arr[i+1])
        if i == len(arr)-2:
            return(max_index)


def find_start_pos(arr):
    min_index = len(arr)-1
    for i in range (len(arr)-1 , 1 , -1):
        if arr[i] < arr[i-1]:
            min_index = arr.index(arr[i-1])
            arr[i], arr[i-1] = arr[i - 1] ,arr[i]
    return (min_index)


def finder(arr):
    if Check_if_sorted(arr) or len(arr) == 1:
        return (-1 , -1)
    else:
        if  arr.index(max(arr)) != len(arr)-1 and arr.index(min(arr)) != 0:
            return ("not sorted at all")
        else:
            print(find_start_pos(arr),',' ,find_last_pos(arr))


arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
finder(arr)