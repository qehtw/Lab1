def Size_of_board(Number, Width, Height):
    if 1 <= Number <= 1012 and 1 <= Width <= 109 and 1 <= Height <= 109:
        left = 1
        right = max(Width, Height) * Number 
        size_of_board = -1

    while left <= right:
        middle = (right + left) // 2

        total = (middle // Width) * (middle // Height)

        if total >= Number:
            right = middle - 1
            size_of_board = middle
        else:
            left = middle + 1


    return size_of_board


print(Size_of_board(4, 1, 1))
