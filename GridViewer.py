
import Maze 


def view(grid):
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


    print("Find a solution to get from ^^ to $$, using the characters " 
        + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'"
        + " (for north, east, south and west).")
    solution = input("Your solution: ")

    currentRow = 1
    currentCol = 0
    done = False
    solved = False
    charIndex = 0
    solutionLength = len(solution)

    while not done and charIndex < solutionLength:
        
        direction = solution[charIndex]
        print("Location: (" + str(currentRow) + ", " + str(currentCol) 
            + "), next direction: '" + direction + "'")
        
        if direction == NORTH:
            currentRow -= 1
            
        elif direction == EAST:
            currentCol += 1
                
        elif direction == SOUTH:
            currentRow += 1
                
        elif direction == WEST:
            currentCol -= 1
        
        else:
            print("MESSAGE 1") # Invalid direction.
        
        if (currentRow < 0 or currentCol < 0 
                        or currentRow >= len(grid) 
                        or currentCol >= len(grid[currentRow])):
            done = True
            print("MESSAGE 2") # Out of bounds.
            
        else:
            if grid[currentRow][currentCol] == Maze.EMPTY:
                grid[currentRow][currentCol] = VISITED
                
            elif grid[currentRow][currentCol] == Maze.WALL:
                done = True
                print("MESSAGE 3") # Hit wall.

            elif grid[currentRow][currentCol] == Maze.END:
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
