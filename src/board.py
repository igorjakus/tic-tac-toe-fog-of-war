class Board:
    def __init__(self, settings):
        self.grid_size = settings.cell_size  # load settings
        self._init_boards()  # init boards
    
    def _init_boards(self):
        # true board
        self.board = [[0] * self.grid_size for __ in range(self.grid_size)]

        # perspective of first / second player (includes fog)
        self.first_player = [[0] * self.grid_size for __ in range(self.grid_size)]
        self.second_player = [[0] * self.grid_size for __ in range(self.grid_size)]   

    def reset(self):
        self._init_boards()

    def get_board(self, player):
        """ Return the board of the player whose turn it is """
        return self.first_player if player else self.second_player

    def update(self, player, attempted_move):
        """Updates boards based on attempted move"""
        r, c = attempted_move

        FIRST = True
        SECOND = False
        
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
    def selected_square(x, y, cell_size=3):
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
