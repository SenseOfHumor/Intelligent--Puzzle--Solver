import copy
from queue import PriorityQueue

def display_puzzle(matrix: list) -> None:
    '''
    Display the 3x3 puzzle matrix

    Extended description of function:
    Function takes in a list of 9 elements and displays them in a 3x3 matrix format.

    Returns: None
    '''
    print()
    for i in range(3):
        for j in range(i*3, i*3+3):
            print("|" , end="")
            print(f"__{matrix[j]}__|" , end="")
        print("\n")

def check_goal(matrix: list) -> bool:
    '''
    Check if the matrix is in the goal state

    Extended description of function:
    Function takes in a list of 9 elements and checks if it is in the goal state.

    Returns: bool
    '''
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return matrix == goal

def check_heuristic(matrix: list) -> int:
    '''
    Calculate the heuristic value of the matrix

    Extended description of function:
    Using the sum of misplaced tiles heuristic, the function calculates the heuristic value of the matrix.

    Returns: int
    '''
    sum = 0
    for index, value in enumerate(matrix):
        if index != value:
            sum += 1
    return sum

def check_valid_matrix(matrix: list) -> bool:
    '''
    Check for matrix validity

    Extended description of function:
    Function checks if the matrix is a valid 3x3 matrix with values between 0 and 8, with no duplicates.

    Returns: bool
    '''
    map = {}

    ## Check for valid length
    if len(matrix) != 9:
        print("Invalid Matrix, must have 9 elements")
        return False
    
    ## Check for valid value range
    for i in matrix:
        if i < 0 or i > 8:
            print(f"Invalid Matrix, value ({i}) at index [{matrix.index(i)}] must be between [0 and 8]")
            return False
    
    ## Check for duplicates
    for i in matrix:
        if i in map:
            print(f"Invalid Matrix, value ({i}) at index [{matrix.index(i)}] has a duplicate")
            return False
        map[i] = matrix[i]
    
    return True

def move_up(matrix_original: list) -> list:
    '''
    Move the blank tile up

    Extended description of function:
    Function takes in a list of 9 elements and moves the blank tile up by swapping it with the tile above it.

    Returns: list
    '''
    matrix = copy.deepcopy(matrix_original)
    index = matrix.index(0)
    if index < 3:
        return matrix
    matrix[index], matrix[index-3] = matrix[index-3], matrix[index]
    return matrix

def move_down(matrix_original: list) -> list:
    '''
    Move the blank tile down

    Extended description of function:
    Function takes in a list of 9 elements and moves the blank tile down by swapping it with the tile below it.

    Returns: list
    '''
    matrix = copy.deepcopy(matrix_original)
    index = matrix.index(0)
    if index > 5:
        return matrix
    matrix[index], matrix[index+3] = matrix[index+3], matrix[index]
    return matrix

def move_left(matrix_original: list) -> list:
    '''
    Move the blank tile left

    Extended description of function:
    Function takes in a list of 9 elements and moves the blank tile left by swapping it with the tile to its left.

    Returns: list
    '''
    matrix = copy.deepcopy(matrix_original)
    index = matrix.index(0)
    if index % 3 == 0:
        return matrix
    matrix[index], matrix[index-1] = matrix[index-1], matrix[index]
    return matrix

def move_right(matrix_original: list) -> list:
    '''
    Move the blank tile right

    Extended description of function:
    Function takes in a list of 9 elements and moves the blank tile right by swapping it with the tile to its right.

    Returns: list
    '''
    matrix = copy.deepcopy(matrix_original)
    index = matrix.index(0)
    if index % 3 == 2:
        return matrix
    matrix[index], matrix[index+1] = matrix[index+1], matrix[index]
    return matrix

def solve_puzzle(start_state):
    '''
    Solve the 8-puzzle using A* algorithm

    Extended description of function:
    Function takes in the start state of the 8-puzzle and solves it using the A* algorithm.

    Returns: None
    '''
    open_list = PriorityQueue()  # Priority queue to store (f(n), state)
    closed_list = set()  # Set to track visited states

    # Add the start state to the open list
    g_score = 0  # Cost to reach the current state
    h_score = check_heuristic(start_state)
    open_list.put((h_score + g_score, g_score, start_state))

    while not open_list.empty():
        _, g_score, current_state = open_list.get()

        print("Exploring State:")
        display_puzzle(current_state)

        # Check if the goal state
        if check_goal(current_state):
            print("Goal State Reached!")
            display_puzzle(current_state)
            return
        closed_list.add(tuple(current_state))

        # Generate all possible moves
        possible_moves = [
            move_up(current_state),
            move_down(current_state),
            move_left(current_state),
            move_right(current_state),
        ]

        for new_state in possible_moves:
            if tuple(new_state) in closed_list:
                continue  # Skip visited

            h_score = check_heuristic(new_state)
            f_score = g_score + 1 + h_score  # f(n) = g(n) + h(n) -> A* heuristic
            open_list.put((f_score, g_score + 1, new_state))

    print("No solution found!")


# Test the functions -> Comment this part to use your own input

####################################
lst = [1, 2, 3, 0, 4, 6, 7, 5, 8]
print("Initial State:")
display_puzzle(lst)
####################################

# Take input from user -> Uncomment this part to take input from user
# lst = []
# for i in range(9):
#     lst.append(int(input(f"Enter value at index {i}: "))
# print("Initial State:")
# display_puzzle(lst)

# Solve the puzzle
solve_puzzle(lst)


