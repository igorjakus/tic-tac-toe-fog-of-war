from random import shuffle, choice
from itertools import permutations
from collections import defaultdict


# Tic-tac-toe board
# 0 1 2
# 3 4 5
# 6 7 8


def who_won(board):
    # -1 black, 0 draw, 1 white
    rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    cols = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    diagonals = [[0, 4, 8], [2, 4, 6]]

    for line in rows + cols + diagonals:
        if all(board[i] == 1 for i in line):
            return 1
        if all(board[i] == -1 for i in line):
            return -1

    return 0


def is_done(board):
    return 0 not in board


def generate_random_play():
    lst = list(range(9))
    shuffle(lst)
    return iter(lst)


def simulate_game(white_moves, black_first=False):
    white_moves = iter(white_moves)
    black_moves = generate_random_play()

    if black_first:
        white_moves, black_moves = black_moves, white_moves

    board = [0] * 9

    for __ in range(5):
        white_move = next(white_moves)
        while board[white_move] == -1:
            white_move = next(white_moves)
        board[white_move] = 1

        if is_done(board):
            return who_won(board)

        black_move = next(black_moves)
        while board[black_move] == 1:
            black_move = next(black_moves)
        board[black_move] = -1

    raise IndexError("coś zepsułem")


def monte_carlo(games, black_first=False, perms=list(permutations(range(9))), i=1):
    balance = defaultdict(int)

    for bot_moves in perms:
        for __ in range(games):
            result = simulate_game(bot_moves, black_first)

            if not black_first:
                balance[bot_moves] += result
            else:
                balance[bot_moves] -= result

    best_perms = sorted(balance, key=balance.get, reverse=True)

    print(f"Finished {i}th depth")
    if len(best_perms) <= 50:
        print("Best win-lose-draw balance:", balance[best_perms[0]], f"of {games} games.")
        return best_perms[:5]

    next_population = best_perms[: len(perms) // 10]
    return monte_carlo(games * 4, black_first, next_population, i + 1)


def try_best_bot(white_sequences, black_sequences, games):
    wins = 0
    draws = 0
    for __ in range(games // 2):
        result = simulate_game(choice(white_sequences))
        wins += result == 1
        draws += result == 0

    for __ in range(games // 2):
        result = simulate_game(choice(black_sequences), black_first=True)
        wins += result == -1
        draws += result == 0

    print("Win-ratio", wins / games)
    print("Draw-ratio", draws / games)
    print("Lose-ratio", (games - wins - draws) / games)


# white, 50, 4, 10 top 5:
best_white = [
    (0, 4, 6, 3, 8, 2, 1, 7, 5),
    (0, 4, 2, 1, 8, 6, 5, 7, 3),
    (0, 4, 1, 2, 8, 3, 7, 5, 6),
    (4, 0, 6, 2, 8, 1, 3, 5, 7),
    (4, 0, 2, 6, 8, 3, 1, 7, 5),
]

# black, 50, 4, 10 top 5:
best_black = [
    (4, 0, 2, 6, 8, 1, 3, 7, 5),
    (4, 0, 6, 8, 2, 3, 1, 5, 7),
    (4, 0, 2, 8, 6, 1, 3, 7, 5),
    (4, 6, 0, 2, 8, 3, 1, 5, 7),
    (4, 0, 6, 8, 2, 3, 5, 1, 7),
]

# Win-ratio 0.81196
# Draw-ratio 0.05562
# Lose-ratio 0.13242
try_best_bot(best_white, best_black, 100_000)


# do generowania rozw
# print(monte_carlo(50, black_first=False))
