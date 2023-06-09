def print_board(board):
    print("  1 2 3")
    for i in range(3):
        row = board[i]
        print(f"{i+1} {' '.join(row)}")

def get_move(player):
    while True:
        try:
            move = input(f"{player}, enter your move (row, column): ")
            row, col = map(int, move.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return (row-1, col-1)
        except ValueError:
            pass
        print("Invalid move. Please try again.")

def check_win(board):
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def play_game():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    while True:
        print_board(board)
        move = get_move(players[current_player])
        if board[move[0]][move[1]] == " ":
            board[move[0]][move[1]] = players[current_player]
            if check_win(board):
                print_board(board)
                print(f"{players[current_player]} wins!")
                break
            elif all(" " not in row for row in board):
                print_board(board)
                print("Tie game!")
                break
            else:
                current_player = (current_player + 1) % 2
        else:
            print("That space is already taken. Please try again.")

play_game()
