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
    
print_board(board)

# make a func. to check whether the space is free or not 
def is_space_free(position):
    if board[position] == ' ':
        return True 
    else:
        return False
    
# make checker functions 
def check_draw():
    for position  in board.keys():
        if board[position] == ' ':
            return False
    return True


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
    
# make a func. to insert letter X or O in a specific position 
def insert_letter(letter, position):
    if is_space_free(position):
        board[position] = letter
        print_board(board)

        if check_win():
            if letter == 'o':
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
        
        
    
player = 'x'
computer = 'o'

def player_move():
    pos = int(input("Enter a position for 'x' :  " ))
    insert_letter(player, pos)

    

def cmp_move():
    pos = int(input("Enter a position for 'o' :  " ))
    insert_letter(computer, pos)
    
    
    
while not check_win():
    cmp_move()
    player_move()
