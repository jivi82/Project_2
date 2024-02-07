"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jiri Vitouch
email: jivi@centrum.cz
discord: jirkav._
"""
# greeting
separator = "=" * 44
print("Welcome to Tic Tac Toe")
print(separator,end="")

# game rules
game_rules = '''
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
'''
print(game_rules,end="")
print(f"{separator}\nLet's start the game\n{"-" * 44}")

# game grid
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

grid_separator = "+---" * 3 + "+"

def display_board():
    print(grid_separator)
    for row in board:
        print("| {0} | {1} | {2} |".format(*row))
        print(grid_separator)

# player move
def get_player_move(current_player):
    while True:
        try:
            move = int(input(f"Player {current_player} | Please enter your move number: "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# update board
def update_board(move, player):
    if board[(move-1)//3][(move-1)%3] == " ":
        board[(move-1)//3][(move-1)%3] = player
        return True
    else:
        print("Unfortunately, your selection is taken. Try another, please!")
        return False

# checking winner
def check_winner():
    for row in board:
        if row.count("X") == 3 or row.count("O") == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]!=" ":
            return True
        if board[0][0] == board[1][1] == board[2][2]!=" ":
            return True
        if board[0][2] == board[1][1] == board[2][0]!=" ":
            return True
    return False
    
# checking free positions on the playing field
def check_grid():
    for row in board:
        if " " in row:
            return False
    return True   

# main function
def main():
    display_board()
    print(separator)
    current_player = "X"
    taken_moves = []
    
    def is_valid_move(move):
        return move not in taken_moves

    while True:
        print(separator)
        move = get_player_move(current_player)
        print(separator)
        
        if is_valid_move(move):
            taken_moves.append(move)
            valid_move = update_board(move, current_player)
            
            if valid_move:
                display_board()
                if check_winner():
                    print(f"Congratulations, the player {current_player} WON!")
                    break
                elif check_grid():
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move. Please try again.")
        else:
            print("This move is already taken. Please choose a different number.")

    print("Game over!")

if __name__ == "__main__":
    main()