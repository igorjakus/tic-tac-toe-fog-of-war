import pygame
from src.window import Window
from src.board import Board
from src.settings import Settings
# from src.input import InputHandler


class App:
    def __init__(self):
        pygame.init()
        self.running = True

        # load settings
        self.settings = Settings()
        
        # create window object
        self.window = Window(self.settings)

        # create board object
        self.board = Board(self.settings)

        # first := True, second := False
        self.player = True  

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
        print(mouse_x, mouse_y)

        # get selected square
        r, c = Board.selected_square(mouse_x, mouse_y, cell_size=700 // 3)

        # update board
        if self.board.update(self.player, (r, c)):
            self.player = not self.player  # update player

    def _handle_keydown(self, event):
        if event.key == pygame.K_q:
            self.running = False
        elif event.key == pygame.K_r:
            self._reset()

    def _on_loop(self):
        pass

    def _on_render(self):
        board = self.board.get_board(self.player)
        self.window.draw(board)
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
