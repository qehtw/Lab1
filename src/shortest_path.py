def is_valid_move(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1


def find_start_points(grid):
    rows, cols = len(grid), len(grid[0])
    return [(i, 0) for i in range(rows) if grid[i][0] == 1]


def find_shortest_path(start_nodes, grid):
    shortest_path_list = []
    for start_point in start_nodes:
        visited = []
        from_to = {}
        queue = [(start_point, [])]
        while queue:
            node, path = queue.pop(0)
            path.append(node)
            visited.append(node)

            if node[1] == len(grid[0]) - 1:
                shortest_path_list.append(len(path))
                find_path(from_to, node, path)

            neighboring_nodes = get_neighbors(grid, node[1], node[0])
            for neighbor in neighboring_nodes:
                if neighbor not in visited:
                    queue.append((neighbor, path[:]))
                    from_to[neighbor] = node

    return min(shortest_path_list) if shortest_path_list else -1


def find_path(from_to, node, path):
    for i in range(len(path) - 1):
        node = from_to[node]


def get_neighbors(grid, y, x):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if grid[x][y] == 0:
        directions.extend([(1, 1), (-1, 1), (-1, -1), (1, -1)])
    neighbors = []
    for col, row in directions:
        new_x, new_y = x + row, y + col
        if is_valid_move(grid, new_x, new_y):
            neighbors.append((new_x, new_y))
    return neighbors


def make_neighbors_zero(grid):
    mines_positions = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[x][y] == 0:
                mines_positions.append([x, y])
    for position in mines_positions:
        position_neighbors = get_neighbors(grid, position[1], position[0])
        for y, x in position_neighbors:
            grid[x][y] = 0
    return grid


def the_shortest_safe_path(grid):
    if not grid or not grid[0]:
        return -1
    grid_without_hidden_mines = make_neighbors_zero(grid)
    start_points = find_start_points(grid_without_hidden_mines)
    if not start_points:
        return -1
    return find_shortest_path(start_points, grid_without_hidden_mines)


import os


def read_input(file_name):
    input_matrix = []
    cur_path = os.path.dirname(__file__)
    resources_dir = os.path.join(cur_path, "..", "test", "resources")
    file_path = os.path.join(resources_dir, file_name)

    with open(file_path, "r") as file:
        for line in file:
            row = list(map(int, line.split()))
            input_matrix.append(row)

    return input_matrix


def write_output(filename, result):
    cur_path = os.path.dirname(__file__)
    resources_dir = os.path.join(cur_path, "..", "test", "resources")
    file_path = os.path.join(resources_dir, filename)

    with open(file_path, "w") as file:
        file.write(str(result))


def find_shortest_safe_path(file_input, file_output):
    grid = read_input(file_input)
    result = the_shortest_safe_path(grid)
    write_output(file_output, result)


def main():
    find_shortest_safe_path("input.txt", "output.txt")


main()
