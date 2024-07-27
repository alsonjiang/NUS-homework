
def solve_maze(maze):
    # Define the possible movements (up, right, down, left)
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    # Helper function to check if a move is valid
    def is_valid(x, y):
        if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 0:
            return True
        return False

    # Recursive function to perform the DFS
    def dfs(x, y):
        # If we've reached the bottom-right cell, we've found the exit
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            return True
        
        # Mark the current cell as part of the path
        maze[x][y] = '.'

        # Explore all possible movements
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            
            if is_valid(new_x, new_y):
                if dfs(new_x, new_y):
                    return True
        
        # Backtrack: unmark the current cell as it leads to no solution
        maze[x][y] = 0
        return False
    
    # Start the maze solving from the top-left cell
    if not dfs(0, 0):
        return "No solution found"
    
    # Mark the start and end positions explicitly if desired
    maze[0][0] = 'S'
    maze[len(maze) - 1][len(maze[0]) - 1] = 'E'
    
    return maze

# Example maze: 0 are paths, 1 are walls
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

# Solve the maze
solved_maze = solve_maze(maze)

# Print the maze with the solution path
for row in solved_maze:
    print(" ".join(str(cell) for cell in row))
