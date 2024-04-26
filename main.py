import pygame


class App:
    def __init__(self):
        pygame.init()
        self.running = True
        self.window = None

        # set icon
        icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("TicTacToe - fog of war @igorjakus")

        # create a surface on screen that has the size of 800 x 800
        screen = pygame.display.set_mode((800, 800))

    def on_event(self, event):
        """Handles all events"""
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


class Window:
    def __init__(self):
        pass


class Board:
    def __init__(self):
        self.board = [0] * 9


if __name__ == "__main__":
    app = App()
    app.run()
