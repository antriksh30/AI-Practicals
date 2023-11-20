from os import system
from time import sleep
import random

def clear_screen():
    system("cls")

def print_board(board):
    print("\n".join([
        "╔════╦════╦════╗",
        "║ {} ║ {} ║ {} ║".format(*board[0:3]),
        "╠════╬════╬════╣",
        "║ {} ║ {} ║ {} ║".format(*board[3:6]),
        "╠════╬════╬════╣",
        "║ {} ║ {} ║ {} ║".format(*board[6:9]),
        "╚════╩════╩════╝",
        "\n"
    ]))

def check_win(board, mark):
    possible_wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 6]]
    return any(all(board[i] == mark for i in win) for win in possible_wins)

def check_draw(board):
    return "  " not in board

def make_human_move(board, player, mark):
    try:
        row, column = map(int, input(f"Enter the row and column to place {mark}: ").split(","))
        position = 3 * (row - 1) + (column - 1)
        if 0 <= position < 9 and board[position] == "  ":
            board[position] = mark
            # clear_screen()
            print_board(board)
        else:
            print("Invalid position!")
            make_human_move(board, player, mark)
    except (ValueError, KeyboardInterrupt):
        print("Invalid input! Please enter row and column separated by a comma.")
        make_human_move(board, player, mark)

def find_winning_move(board, mark):
    for i in range(9):
        if board[i] == "  ":
            board[i] = mark
            if check_win(board, mark):
                board[i] = "  "
                return i
            board[i] = "  "
    return None

def make_computer_move(board, mark):
    winning_move = find_winning_move(board, mark)
    if winning_move is not None:
        board[winning_move] = mark
    else:
        opponent_mark = "X " if mark == "O " else "O "
        blocking_move = find_winning_move(board, opponent_mark)
        if blocking_move is not None:
            board[blocking_move] = mark
        else:
            available_positions = [i for i in range(9) if board[i] == "  "]
            random_move = random.choice(available_positions)
            board[random_move] = mark

    # clear_screen()
    print_board(board)

def main():
    try:
        # system("cls")
        print("TIC TAC TOE GAME!")
        print("Player 1 will play with X and computer will play with O")
        sleep(1)
        print("The positions are numbered as shown below:")
        print("\n".join([
            "╔═════╦═════╦═════╗",
            "║ 2,1 ║ 2,2 ║ 2,3 ║",
            "╠═════╬═════╬═════╣",
            "║ 1,1 ║ 1,2 ║ 1,3 ║",
            "╠═════╬═════╬═════╣",
            "║ 3,1 ║ 3,2 ║ 3,3 ║",
            "╚═════╩═════╩═════╝",
            "\n"
        ]))
        sleep(1)
        print("LETS START!!")
        sleep(3)
        # system("cls")

        player1 = input("Enter the name of Player 1: ")
        player2 = "Computer"

        sleep(1)
        player = random.choice([player1, player2])

        board = ["  "] * 9
        print_board(board)

        while True:
            print('\n' + player + "'s turn")
            mark = "X " if player == player1 else "O "

            if player == player1:
                make_human_move(board, player, mark)
            else:
                make_computer_move(board, mark)

            if check_win(board, mark):
                print(player, "wins!")
                print()
                return
            if check_draw(board):
                print("It's a draw!")
                print()
                return
            player = player2 if player == player1 else player1

    except KeyboardInterrupt:
        print("\n\nGame interrupted!")

if __name__ == "__main__":
    main()