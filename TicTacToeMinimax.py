def display_board(board):
    print("╔═══╦═══╦═══╗")
    print(f'║ {board[0][0]} ║ {board[0][1]} ║ {board[0][2]} ║')
    print("╠═══╬═══╬═══╣")
    print(f'║ {board[1][0]} ║ {board[1][1]} ║ {board[1][2]} ║')
    print("╠═══╬═══╬═══╣")
    print(f'║ {board[2][0]} ║ {board[2][1]} ║ {board[2][2]} ║')
    print("╚═══╩═══╩═══╝")
    print()

def is_space_free(board, position):
    row, col = divmod(position - 1, 3)
    return board[row][col] == ' '

def insert_letter(board, letter, position):
    row, col = divmod(position - 1, 3)
    if is_space_free(board, position):
        board[row][col] = letter
        display_board(board)
        if check_draw(board):
            print("It's a Draw!")
            print()
            exit()
        if check_for_win(board, letter):
            if letter == 'X':
                print("Bot wins!")
            else:
                print("Player wins!")
            print()
            exit()
    else:
        print("Can't insert there!")
        print()

def check_for_win(board, letter):
    for row in board:
        if all(cell == letter for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == letter for row in range(3)):
            return True

    if all(board[i][i] == letter for i in range(3)) or all(board[i][2 - i] == letter for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board):
    position = int(input("Please enter a position (1-9): "))
    insert_letter(board, player, position)

def comp_move(board):
    best_score = -800
    best_move = 0
    alpha = -800  # Initialize alpha and beta
    beta = 800
    for position in range(1, 10):
        if is_space_free(board, position):
            row, col = divmod(position - 1, 3)
            board[row][col] = bot
            score = minimax(board, 0, alpha, beta, False)
            board[row][col] = ' '
            if score > best_score:
                best_score = score
                best_move = position
            alpha = max(alpha, best_score)
    insert_letter(board, bot, best_move)


def minimax(board, depth, alpha, beta, is_maximizing):
    if check_for_win(board, bot):
        return 1
    if check_for_win(board, player):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -800
        for position in range(1, 10):
            if is_space_free(board, position):
                row, col = divmod(position - 1, 3)
                board[row][col] = bot
                score = minimax(board, depth + 1, alpha, beta, False)
                board[row][col] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 800
        for position in range(1, 10):
            if is_space_free(board, position):
                row, col = divmod(position - 1, 3)
                board[row][col] = player
                score = minimax(board, depth + 1, alpha, beta, True)
                board[row][col] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score


board = [[' ' for _ in range(3)] for _ in range(3)]
display_board(board)
print("Computer goes first! Good luck.")
print("Positions are as follows:")
print("╔═══╦═══╦═══╗")
print("║ 1 ║ 2 ║ 3 ║")
print("╠═══╬═══╬═══╣")
print("║ 4 ║ 5 ║ 6 ║")
print("╠═══╬═══╬═══╣")
print("║ 7 ║ 8 ║ 9 ║")
print("╚═══╩═══╩═══╝")
print("")

player = 'O'
bot = 'X'

while not check_for_win(board, player):
    comp_move(board)
    player_move(board)