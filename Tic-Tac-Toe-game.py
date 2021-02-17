'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2
  1,0 | 1,1 | 1,2
  2,0 | 2,1 | 2,2
'''
N = 3
grid =[[" "]*N,[" "]*N,[" "]*N]

#This function prints the grid of Tic-Tac-Toe as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('--' + '---' * N + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * N + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win():

    if grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid [0][0] !=' ' :
        return True
    elif grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid [1][0] !=' ' :
        return True
    elif grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid [2][0] !=' ' :
        return True
    elif grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid [0][0] !=' ' :
        return True
    elif grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid [0][1] !=' ' :
        return True
    elif grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid [0][2] !=' ' :
        return True
    elif grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid [0][0] !=' ' :
        return True
    elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid [0][2] !=' ' :
        return True

#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
        i=0
        j=0
        while i <=2 :
            j=0
            while j <=2:
                if grid [i][j] == ' ':
                    return False
                j+=1
            i+=1
        return True




#This function checks if given cell is empty or not
def check_empty(i, j):
   if grid[i][j] == ' ':
       return True


#This function checks if given position is valid or not
def check_valid_position(i, j):
    if(0<=i<=2 and 0<=j<=2):
        return True


#This function sets a value to a cell
def set_cell(i, j, mark):
    grid[i][j]=i,j
    grid[i][j]=mark

#This function clears the grid
def grid_clear():
    for i in range(N):
        for j in range(N):
            grid[i][j]=' '

#MAIN FUNCTION
def play_game():
    print("Tic-Tac-Toe Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Takes input from the user to fill in the grid
        print('Player %s' % mark)
        i, j = map(int, input('Enter the row index and column index: ').split())
        while not check_valid_position(i, j) or not check_empty(i,j):
            i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
        #Set the input position with the mark
        set_cell(i, j, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        #Check if the state of the grid has a tie state
        if check_tie(mark):
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break
        #Player number changes after each turn
        player = 1 - player


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
