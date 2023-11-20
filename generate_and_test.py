def solve_maze(maze):
    # Get the dimensions of the maze
    rows = len(maze)
    cols = len(maze[0])

    # Helper function to check if a position is valid and not visited
    def is_valid(row, col, visited):
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 1 and (row, col) not in visited

    # Helper function to recursively generate and test paths
    def generate_and_test(row, col, path, visited):
        # Base case: reached the bottom right corner
        if row == rows - 1 and col == cols - 1:
            return path

        # Mark the current position as visited
        visited.add((row, col))

        # Try moving down
        if is_valid(row + 1, col, visited):
            result = generate_and_test(row + 1, col, path + [(row + 1, col)], visited)
            if result:
                return result

        # Try moving right
        if is_valid(row, col + 1, visited):
            result = generate_and_test(row, col + 1, path + [(row, col + 1)], visited)
            if result:
                return result

        # Try moving up
        if is_valid(row - 1, col, visited):
            result = generate_and_test(row - 1, col, path + [(row - 1, col)], visited)
            if result:
                return result

        # Try moving left
        if is_valid(row, col - 1, visited):
            result = generate_and_test(row, col - 1, path + [(row, col - 1)], visited)
            if result:
                return result

        # If no valid moves, mark the current position as unvisited
        visited.remove((row, col))

    # Start the generate and test algorithm from the top left corner
    start_row = 0
    start_col = 0
    start_path = [(start_row, start_col)]
    start_visited = set()
    solution = generate_and_test(start_row, start_col, start_path, start_visited)

    if solution:
        # Create a solution matrix with the same dimensions as the maze
        solution_matrix = [[0] * cols for _ in range(rows)]

        # Mark the path taken by the algorithm with 'X'
        for row, col in solution:
            solution_matrix[row][col] = '1'

        return solution_matrix
    else:
        return "No solution"

maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

solution = solve_maze(maze)
if solution == "No solution":
    print("No solution found")
else:
    print("Path exists, here is the path: ")
    for row in solution:
        print(*row)
