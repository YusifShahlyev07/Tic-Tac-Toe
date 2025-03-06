#Tic Tac Toe 
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

winner = None
game_running = True
current_player = "X"

def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def player_input(board):
    player_input = int(input("Type a number between 1-9 : "))
    if board[player_input-1] == "-":
        board[player_input-1] = current_player
    else:
        print("this number was choosen")

def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif  board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif  board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif  board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif  board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_inclined(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It is Tie")
        game_running = False

def check_win():
    global game_running
    if check_horizontal(board) or check_vertical(board) or check_inclined(board) == True:
        print(f"The winner is {current_player}")
        game_running = False

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

while game_running :
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    
