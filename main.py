import pygame


class App:
    def __init__(self):
        pygame.init()
        self.running = True
        self.window = Window(
            shape=(700, 700), grid_size=3
        )  # later get it from settings.json

        self.board = Board(grid_size=3)
        self.board = [[0, 0, 0] for __ in range(3)]

        self.player = True  # first := True, second := False

    def _on_input(self):
        """Handles all inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # handle mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse()

            # handle keyboard
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)

    def _handle_mouse(self):
        # get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

    def _handle_keydown(self, event):
        if event.key == pygame.K_q:
            self.running = False
        elif event.key == pygame.K_r:
            self._reset()

    def _on_loop(self):
        self.player = not self.player

    def _on_render(self):
        self.window.draw(self.board)
        pygame.display.flip()

    def _on_cleanup(self):
        pygame.quit()

    def _reset(self):
        self.board.reset()

    def run(self):
        while self.running:
            self._on_input()
            self._on_loop()
            self._on_render()
        self._on_cleanup()


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


class Board:
    def __init__(self, grid_size):
        self.grid_size = grid_size

        # true board
        self.board = [[0] * grid_size for __ in range(grid_size)]

        # perspective of first/second player (includes fog)
        self.board = [[0] * grid_size for __ in range(grid_size)]
        self.board = [[0] * grid_size for __ in range(grid_size)]

    def reset(self):
        self.__init__(self.grid_size)

    def get_first_player():
        pass

    def get_second_player():
        pass

    def update(player, attempted_move):
        """ Updates boards based on attempted move """
        pass

    @staticmethod
    def at_linear(x, y, grid_size=3):
        """Cartesian (x,y) to linear index i
        Ex. (1, 0) -> 1, (2,2) -> 8"""
        return y * grid_size + x


if __name__ == "__main__":
    app = App()
    app.run()
