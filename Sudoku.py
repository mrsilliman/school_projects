# Principles of Computing Python
# Final Capstone Project
# SIMPLE SUDOKU SOLVER GAME
# Mary Silliman

# welcome user
print(f'Hello! Welcome to the SIMPLE SUDOKU SOLVER!')

# prompt user to enter number between 1-20
# loop if response is invalid
invalid_response = True
while invalid_response:
    user_choice = input('\nEnter a number between 1-20 to generate a sudoku: ')
    if user_choice.isdigit() and (int(user_choice) > 1 and int(user_choice) < 20):
        invalid_response = False
    else:
        print(f'Invalid answer. Try again')

# import Sudoku_Boards.py file
# assign and print uncompleted sudoku grid based on user response
from Sudoku_Boards import sudoku_boards
grid = sudoku_boards[int(user_choice)]
print(f'\nHere\'s your sudoku board. Zeros represent blank spaces.')
print(grid)

# find missing values in each row, requires row call
def set_rows(row):
    missing_rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in grid[row,]:
        if i == 0:
            continue
        elif i in missing_rows:
            missing_rows.remove(i)
    return missing_rows

# find missing values in each column, requires column call
def set_columns(column):
    missing_cols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in grid[:,column]:
        if i == 0:
            continue
        elif i in missing_cols:
            missing_cols.remove(i)
    return missing_cols

# find missing values in each 3x3 square, requires row and column start and end calls
def three_by_three(r_start, r_end, c_start, c_end):
    templist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(r_start, r_end):
        for j in range(c_start, c_end):
            if grid[i][j] == 0:
                continue
            elif grid[i][j] in templist:
                templist.remove(grid[i][j])
    return templist

# isolate specific 3x3 grid
def incorporate_threes(row, col):
    box = None
    if row < 3 and col < 3:
        box = three_by_three(0, 3, 0, 3)
    elif row < 3 and col < 6:
        box = three_by_three(0, 3, 3, 6)
    elif row < 3 and col < 9:
        box = three_by_three(0, 3, 6, 9)
    elif row < 6 and col < 3:
        box = three_by_three(3, 6, 0, 3)
    elif row < 6 and col < 6:
        box = three_by_three(3, 6, 3, 6)
    elif row < 6 and col < 9:
        box = three_by_three(3, 6, 6, 9)
    elif row < 9 and col < 3:
        box = three_by_three(6, 9, 0, 3)
    elif row < 9 and col < 6:
        box = three_by_three(6, 9, 3, 6)
    elif row < 9 and col < 9:
        box = three_by_three(6, 9, 6, 9)
    return box

# call functions to find common missing values amongst rows, columns, 3x3
def solve_sudoku():
    for row in range(0,9):
        for col in range(0,9):
            trial_1 = set(set_rows(row)).intersection(set(set_columns(col)))
            trial_2 = list(set(trial_1).intersection(set(incorporate_threes(row, col))))

            if grid[row][col] == 0:
                if len(set_rows(row)) == 1 and len(set_columns(col)) == 0:
                    grid[row][col] = set_rows(row)[0]
                elif len(set_rows(row)) == 0 and len(set_columns(col)) == 1:
                    grid[row][col] = set_columns(col)[0]
                elif len(trial_1) == 1:
                    trial_1 = list(trial_1)
                    grid[row][col] = trial_1[0]
                elif len(trial_2) == 1:
                    grid[row][col] = trial_2[0]

# prompt user to solve the sudoku or receive the completed board
game_choices = [1, 2]
game_decision = int(input('\nWould you like to try solving the sudoku or give up? (Enter \'1\' to solve, \'2\' to give up): '))
while game_decision not in game_choices:
    print(f'Invalid answer. Try again')
    game_decision = int(input('\nWould you like to try solving the sudoku or give up? (Enter 1 to solve, 2 to give up): '))

if game_decision == 1:
    input(f'\nEnter any response when you solve the sudoku. ')
    print('Great game! Thanks for playing!')
else:
    while 0 in grid:    # call function until all empty spaces (zeros) are filled
        solve_sudoku()
    else:
        print(f'\nGood try! Here\'s the solved sudoku.')
        print(f'Thanks for playing!')
        print(grid)     # print completed sudoku grid