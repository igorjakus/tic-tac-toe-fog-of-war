import pygame


class Window:
    def __init__(self, shape, grid_size):
        # setup screen
        self.screen = pygame.display.set_mode((shape[0], shape[1]))

        self.shape = shape
        self.grid_size = grid_size
        self.cell_size = shape[0] // grid_size

        # setup icon
        icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("TicTacToe - fog of war @igorjakus")

    def draw(self, board):
        self._draw_board()
        self._draw_symbols(board)
        self._draw_fog(board)

    def _draw_board(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BOLDNESS = 3
        CELL_SIZE = self.cell_size
        WINDOW_SIZE = self.shape[0]

        # Rysuj planszę
        self.screen.fill(WHITE)

        # Rysuj linie siatki
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                BLACK,
                (0, i * CELL_SIZE),
                (WINDOW_SIZE, i * CELL_SIZE),
                BOLDNESS,
            )
            pygame.draw.line(
                self.screen,
                BLACK,
                (i * CELL_SIZE, 0),
                (i * CELL_SIZE, WINDOW_SIZE),
                BOLDNESS,
            )

    # Rysuj znaki na planszy
    def _draw_symbols(self, board):
        BLACK = (0, 0, 0)
        CELL_SIZE = self.cell_size

        for row in range(3):
            for col in range(3):
                if board[row][col] == -1:
                    pygame.draw.line(
                        self.screen,
                        BLACK,
                        (col * CELL_SIZE + 20, row * CELL_SIZE + 20),
                        ((col + 1) * CELL_SIZE - 20, (row + 1) * CELL_SIZE - 20),
                        5,
                    )
                    pygame.draw.line(
                        self.screen,
                        BLACK,
                        ((col + 1) * CELL_SIZE - 20, row * CELL_SIZE + 20),
                        (col * CELL_SIZE + 20, (row + 1) * CELL_SIZE - 20),
                        5,
                    )

                elif board[row][col] == 1:
                    pygame.draw.circle(
                        self.screen,
                        BLACK,
                        (
                            col * CELL_SIZE + CELL_SIZE // 2,
                            row * CELL_SIZE + CELL_SIZE // 2,
                        ),
                        CELL_SIZE // 3,
                        5,
                    )

    def _draw_fog(self, board):
        # draw fog based on player's knowledge
        pass
