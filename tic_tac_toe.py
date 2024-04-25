from random import sample


class Game:
    """Board looks like this:
    0 1 2
    3 4 5
    6 7 8
    """

    def who_won(self):
        # -1 second player, 0 draw, 1 first player
        rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        cols = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        diagonals = [[0, 4, 8], [2, 4, 6]]

        for line in rows + cols + diagonals:
            if all(self.board[i] == 1 for i in line):
                return 1
            if all(self.board[i] == -1 for i in line):
                return -1
        return 0

    def play_game(self, first_player, second_player):
        self.board = [0] * 9

        first_player = iter(first_player)
        black_moves = iter(second_player)

        # first 8 moves
        for __ in range(4):
            move = next(first_player)
            while self.board[move] == -1:
                move = next(first_player)
            self.board[move] = 1

            move = next(black_moves)
            while self.board[move] == 1:
                move = next(black_moves)
            self.board[move] = -1

        # 9th move
        move = next(first_player)
        while self.board[move] == -1:
            move = next(first_player)
        self.board[move] = 1

        return self.who_won()

    def play_against_random(self, player, player_first):
        random_strategy = sample(range(9), 9)
        if player_first:
            return self.play_game(player, random_strategy)
        else:
            return self.play_game(random_strategy, player)
