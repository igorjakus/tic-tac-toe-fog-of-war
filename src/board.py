# const
FIRST = True
SECOND = False


class Board:
    def __init__(self, grid_size):
        self.grid_size = grid_size

        # true board
        self.board = [[0] * grid_size for __ in range(grid_size)]

        # perspective of first/second player (includes fog)
        self.first_player = [[0] * grid_size for __ in range(grid_size)]
        self.second_player = [[0] * grid_size for __ in range(grid_size)]

    def reset(self):
        self.__init__(self.grid_size)

    def get_board(self, player):
        """ Return the board of the player whose turn it is """
        return self.first_player if player else self.second_player

    def update(self, player, attempted_move):
        """Updates boards based on attempted move"""
        r, c = attempted_move

        updated = False

        if player is FIRST:
            # update fog and actual board
            if self.board[r][c] == 0:
                self.board[r][c] = 1
                self.first_player[r][c] = 1
                updated = True
            # update fog
            elif self.board[r][c] == -1:
                self.first_player[r][c] = -1

        elif player is SECOND:
            # update fog and actual board
            if self.board[r][c] == 0:
                self.board[r][c] = -1
                self.second_player[r][c] = -1
                updated = True
            # update fog
            elif self.board[r][c] == 1:
                self.second_player[r][c] = 1

        return updated

    @staticmethod
    def selected_square(x, y, cell_size):
        """Gives (i, j) of selected square by mouse"""
        row = y // cell_size 
        col = x // cell_size
        return row, col

    @staticmethod
    def at_cartesian(index, grid_size=3):
        """Linear index to cartesian point (x, y)"""
        row = index // grid_size
        col = index % grid_size
        return row, col

    @staticmethod
    def at_linear(i, j, grid_size=3):
        """Cartesian (x,y) to linear index i
        Ex. (1, 0) -> 1, (2,2) -> 8"""
        return j * grid_size + i
