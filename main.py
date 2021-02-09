import pygame
from pygame.locals import *

from chess import ChessDesk
import chess


class Figure(pygame.Surface):
    def __init__(self, master, size=(50, 50)):
        super().__init__(size)
        self._screen = master

        self.rect = self.get_rect()

    def set_position(self, position):
        x, y = position

        return self.rect.move_ip(x * 50, y * 50)

    def blit(self):
        return NotImplementedError


class Pawn(Figure, chess.Pawn):
    def __init__(self, screen, position=(0, 0), color='white'):
        super().__init__(screen)
        self.set_position(position)
        self._color = color

    def blit(self):
        image = pygame.image.load(f"img/pawn-{self._color}.png")
        self._screen.blit(image, self.rect)


class King(Figure):
    def __init__(self, screen, position=(0, 0), color='white'):
        super().__init__(screen)
        self.set_position(position)
        self._color = color

    def blit(self):
        image = pygame.image.load(f"img/king-{self._color}.png")
        self._screen.blit(image, self.rect)


class Queen(Figure):
    def __init__(self, screen, position=(0, 0), color='white'):
        super().__init__(screen)
        self.set_position(position)
        self._color = color

    def blit(self):
        image = pygame.image.load(f"img/queen-{self._color}.png")
        self._screen.blit(image, self.rect)


class Knight(Figure):
    def __init__(self, screen, position=(0, 0), color='white'):
        super().__init__(screen)
        self.set_position(position)
        self._color = color

    def blit(self):
        image = pygame.image.load(f"img/knight-{self._color}.png")
        self._screen.blit(image, self.rect)


class Castle(Figure):
    def __init__(self, screen, position=(0, 0), color='white'):
        super().__init__(screen)
        self.set_position(position)
        self._color = color

    def blit(self):
        image = pygame.image.load(f"img/castle-{self._color}.png")
        self._screen.blit(image, self.rect)


class Bishop(Figure):
    def __init__(self, screen, position=(0, 0), color='white'):
        super().__init__(screen)
        self.set_position(position)
        self._color = color

    def blit(self):
        image = pygame.image.load(f"img/bishop-{self._color}.png")
        self._screen.blit(image, self.rect)


class GUI:
    def __init__(self):
        self._chessdesk = ChessDesk()
        self._running = False
        self.size = self.width, self.height = 640, 480


    def _on_init(self):
        pygame.init()

        self._screen = pygame.display.set_mode(
            self.size, 
        )
        self._clock = pygame.time.Clock()
        self._running = True
        self._FPS = 30
        self._playtime = 0

        self.figures = [
            Castle(self._screen, color='white', position=(0, 0)),
            Knight(self._screen, color='white', position=(1, 0)),
            Bishop(self._screen, color='white', position=(2, 0)),
            Queen(self._screen,  color='white', position=(3, 0)),
            King(self._screen,   color='white', position=(4, 0)),
            Bishop(self._screen, color='white', position=(5, 0)),
            Knight(self._screen, color='white', position=(6, 0)),
            Castle(self._screen, color='white', position=(7, 0)),
            Pawn(self._screen, color='white', position=(1, 1)),
            Pawn(self._screen, color='white', position=(0, 1)),
            Pawn(self._screen, color='white', position=(2, 1)),
            Pawn(self._screen, color='white', position=(3, 1)),
            Pawn(self._screen, color='white', position=(4, 1)),
            Pawn(self._screen, color='white', position=(5, 1)),
            Pawn(self._screen, color='white', position=(6, 1)),
            Pawn(self._screen, color='white', position=(7, 1)),

            Castle(self._screen, color='black', position=(0, 7)),
            Knight(self._screen, color='black', position=(1, 7)),
            Bishop(self._screen, color='black', position=(2, 7)),
            Queen(self._screen,  color='black', position=(3, 7)),
            King(self._screen,   color='black', position=(4, 7)),
            Bishop(self._screen, color='black', position=(5, 7)),
            Knight(self._screen, color='black', position=(6, 7)),
            Castle(self._screen, color='black', position=(7, 7)),
            Pawn(self._screen, color='black', position=(1, 6)),
            Pawn(self._screen, color='black', position=(0, 6)),
            Pawn(self._screen, color='black', position=(2, 6)),
            Pawn(self._screen, color='black', position=(3, 6)),
            Pawn(self._screen, color='black', position=(4, 6)),
            Pawn(self._screen, color='black', position=(5, 6)),
            Pawn(self._screen, color='black', position=(6, 6)),
            Pawn(self._screen, color='black', position=(7, 6)),
        ]

        pygame.display.set_caption("Super Chess")

    def _on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def _on_loop(self):
        milliseconds = self._clock.tick(self._FPS) 
        self._playtime += milliseconds / 1000.0 

    def _on_render(self):
        self._screen.fill('white')
        
        [figure.blit() for figure in self.figures]

        pygame.display.flip()

    def _on_cleanup(self):
        pygame.quit()

    def run(self):
        self._on_init()

        while self._running:
            for event in pygame.event.get():
                self._on_event(event)
            self._on_loop()
            self._on_render()

        self._on_cleanup()


if __name__ == "__main__":
     gui = GUI()
     gui.run()