import pygame


class Window:
    def __init__(self, settings):
        # load settings
        self.shape = settings.window_shape
        self.grid_size = settings.grid_size
        self.cell_size = settings.cell_size
        
        # setup screen
        self.screen = pygame.display.set_mode(self.shape)

        # setup icon
        icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("TicTacToe - fog of war @igorjakus")

        # load fog image
        self.margin = 0.9
        fog_img = pygame.image.load("assets/fog.png")
        self.fog_img = pygame.transform.smoothscale(
            fog_img, (self.cell_size * self.margin, self.cell_size * self.margin)
        )

    def draw(self, board):
        BLACK = (0, 0, 0)

        def draw_circle(row, col):
            pygame.draw.circle(
                self.screen,
                BLACK,
                (
                    col * self.cell_size + self.cell_size // 2,
                    row * self.cell_size + self.cell_size // 2,
                ),
                self.cell_size // 3,
                5,
            )

        def draw_cross(row, col):
            pygame.draw.line(
                self.screen,
                BLACK,
                (col * self.cell_size + 20, row * self.cell_size + 20),
                ((col + 1) * self.cell_size - 20, (row + 1) * self.cell_size - 20),
                5,
            )
            pygame.draw.line(
                self.screen,
                BLACK,
                ((col + 1) * self.cell_size - 20, row * self.cell_size + 20),
                (col * self.cell_size + 20, (row + 1) * self.cell_size - 20),
                5,
            )

        def draw_fog(row, col):
            x = (col + ((1 - self.margin) / 2)) * self.cell_size
            y = (row + ((1 - self.margin) / 2)) * self.cell_size
            self.screen.blit(self.fog_img, (x, y))

        # draw grid
        self._draw_grid()

        # draw circles / crosses / fog
        for row in range(3):
            for col in range(3):
                if board[row][col] == 1:
                    draw_circle(row, col)
                elif board[row][col] == -1:
                    draw_cross(row, col)
                else:
                    draw_fog(row, col)

    def _draw_grid(self):
        """Draw grid lines"""
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BOLDNESS = 3
        WINDOW_SIZE = self.shape[0]

        self.screen.fill(WHITE)

        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                BLACK,
                (0, i * self.cell_size),
                (WINDOW_SIZE, i * self.cell_size),
                BOLDNESS,
            )
            pygame.draw.line(
                self.screen,
                BLACK,
                (i * self.cell_size, 0),
                (i * self.cell_size, WINDOW_SIZE),
                BOLDNESS,
            )
