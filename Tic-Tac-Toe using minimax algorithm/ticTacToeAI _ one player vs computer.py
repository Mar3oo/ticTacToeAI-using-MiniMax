# first set the board using a dict
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' ',}

# make a func. to print the board 
def print_board(your_board):
    print(f' {your_board[1]} | {your_board[2]} |  {your_board[3]} ')
    print(f'-----------')
    print(f' {your_board[4]} | {your_board[5]} | {your_board[6]}  ')
    print(f'-----------')
    print(f' {your_board[7]} | {your_board[8]} | {your_board[9]}  ')


# make a func. to check whether the space is free or not 
def is_space_free(position):
    if board[position] == ' ':
        return True 
    else:
        return False


# make a func. to insert letter X or O in a specific position 
def insert_letter(letter, position):
    if is_space_free(position):
        board[position] = letter
        print_board(board)
        print(' ')

        if check_win():
            if letter == 'X':
                print('computer wins!')
                exit()
            else : 
                print('player wins!')
                exit()
                
        if check_draw():
            print('Draw!')
            exit()
        
    
    else :
        print('SOMETHING WENT WRONG !')
        position = int(input('This position is not empty try entering another one : '))
        insert_letter(letter, position)


# make checker functions 

def check_win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def check_who_won(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def check_draw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

# make methods to actually play the game

def player_move():
    position = int(input("Enter the position to put 'X' in :  "))
    insert_letter(player, position)
    return


def cmp_move():
    best_score = -800
    best_move = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = cmp
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > best_score):
                best_score = score
                best_move = key

    insert_letter(cmp, best_move)
    return

# the algorithm => MiniMax
def minimax(board, depth, isMaximizing):
    if (check_who_won(cmp)):
        return 1
    elif (check_who_won(player)):
        return -1
    elif (check_draw()):
        return 0

    if (isMaximizing):
        best_score = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = cmp
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < best_score):
                    best_score = score
        return best_score



print_board(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'X'
cmp = 'O'


global firstComputerMove
firstComputerMove = True

while not check_win():
    cmp_move()
    player_move()
