
import Maze 


def view(grid):
	for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j] == Maze.EMPTY:
                print("  ", end = "")
                    
            elif grid[i][j] == Maze.WALL:
                print("@@", end = "")
                    
            elif grid[i][j] == Maze.START:
                print("^^", end = "")
                    
            elif grid[i][j] == Maze.END:
                print("$$", end = "")
                    
            elif grid[i][j] == Maze.VISITED:
                print("..", end = "")
                    
            else:
                raise AssertionError
            
        print()


    print("Find a solution to get from ^^ to $$, using the characters " 
        + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'"
        + " (for north, east, south and west).")
    solution = input("Your solution: ")

    row = 1
    col = 0
    done = False
    solved = False
    charIndex = 0
    solutionLength = len(solution)

    while not done and charIndex < solutionLength:
        
        direction = solution[charIndex]
        print("Location: (" + str(row) + ", " + str(col) 
            + "), next direction: '" + direction + "'")
        
        if direction == NORTH:
            row -= 1
            
        elif direction == EAST:
            col += 1
                
        elif direction == SOUTH:
            row += 1
                
        elif direction == WEST:
            col -= 1
        
        else:
            print("MESSAGE 1") # Invalid direction.
        
        if (row < 0 or col < 0 
                        or row >= len(grid) 
                        or col >= len(grid[row])):
            done = True
            print("MESSAGE 2") # Out of bounds.
            
        else:
            cell = grid[currentRow][currentCol]
            if cell == Maze.EMPTY:
                cell = VISITED
                
            elif cell == Maze.WALL:
                done = True
                print("MESSAGE 3") # Hit wall.

            elif cell == Maze.END:
                done = True
                solved = True
                print("MESSAGE 4") # Solved.
                
            else:
                pass # Do nothing
        
        charIndex += 1
    # end-while


    if not solved:
        print("MESSAGE 5") # Did not reach the end.


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j] == Maze.EMPTY:
                print("  ", end = "")
                    
            elif grid[i][j] == Maze.WALL:
                print("##", end = "")
                    
            elif grid[i][j] == Maze.START:
                print("^^", end = "")
                    
            elif grid[i][j] == Maze.END:
                print("$$", end = "")
                    
            elif grid[i][j] == Maze.VISITED:
                print("..", end = "")
                    
            else:
                raise AssertionError
            
        print()
