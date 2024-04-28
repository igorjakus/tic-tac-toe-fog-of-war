import pygame


class App:
    def __init__(self):
        pygame.init()
        self.running = True
        self.window = None  # seperate object later in project
        self.WINDOW_SIZE = 700

        # setup icon
        icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("TicTacToe - fog of war @igorjakus")

        # setup screen
        self.screen = pygame.display.set_mode((self.WINDOW_SIZE, self.WINDOW_SIZE))

        self.board = [[0, 0, 0] for __ in range(3)]

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
        pass

    def _on_render(self):
        self._draw_board()
        self._draw_fog()
        self._draw_symbols()
        pygame.display.flip()

    def _draw_board(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BOLDNESS = 3
        CELL_SIZE = self.WINDOW_SIZE // 3

        # Rysuj planszę
        self.screen.fill(WHITE)

        # Rysuj linie siatki
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                BLACK,
                (0, i * CELL_SIZE),
                (self.WINDOW_SIZE, i * CELL_SIZE),
                BOLDNESS,
            )
            pygame.draw.line(
                self.screen,
                BLACK,
                (i * CELL_SIZE, 0),
                (i * CELL_SIZE, self.WINDOW_SIZE),
                BOLDNESS,
            )

    # Rysuj znaki na planszy
    def _draw_symbols(self):
        BLACK = (0, 0, 0)
        CELL_SIZE = self.WINDOW_SIZE // 3

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 1:
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

                elif self.board[row][col] == 2:
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

    def _draw_fog(self):
        # draw fog based on player's knowledge
        pass

    def _on_cleanup(self):
        pygame.quit()

    def _reset(self):
        self.board = [0] * 9

    def run(self):
        while self.running:
            self._on_input()
            self._on_loop()
            self._on_render()
        self._on_cleanup()


class Window:
    def __init__(self):
        pass


class Board:
    def __init__(self, window_size):
        self.GRID_SIZE = 3
        self.WINDOW_SIZE = window_size
        self.CELL_SIZE = window_size // self.GRID_SIZE
        self.board = [0] * (self.GRID_SIZE * self.GRID_SIZE)
    
    def at_cartesian(x, y):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
