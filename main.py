import pygame
from board import Board
from pieces import Bishop, Knight, Pawn, Queen, Rook, King
from constants import PieceColor


class Game:
    """Handles the basic game functions"""

    def __init__(self, width, height):
        self.WIDTH = width // 8 * 8  # Round down to multiple of 8
        self.HEIGHT = height // 8 * 8

    def run(self):
        """Run the game"""
        self.setup()
        self.loop()

    def setup(self):
        """Runs all code needed to setup the game"""
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.board = Board(0, 0, self.HEIGHT)

        self.board.add_piece(Pawn(PieceColor.WHITE), (0, 6))
        self.board.add_piece(Pawn(PieceColor.WHITE), (1, 6))
        self.board.add_piece(Pawn(PieceColor.WHITE), (2, 6))
        self.board.add_piece(Pawn(PieceColor.WHITE), (3, 6))
        self.board.add_piece(Pawn(PieceColor.WHITE), (4, 6))
        self.board.add_piece(Pawn(PieceColor.WHITE), (5, 6))
        self.board.add_piece(Pawn(PieceColor.WHITE), (6, 6))
        self.board.add_piece(Pawn(PieceColor.WHITE), (7, 6))

        self.board.add_piece(Pawn(PieceColor.BLACK), (0, 1))
        self.board.add_piece(Pawn(PieceColor.BLACK), (1, 1))
        self.board.add_piece(Pawn(PieceColor.BLACK), (2, 1))
        self.board.add_piece(Pawn(PieceColor.BLACK), (3, 1))
        self.board.add_piece(Pawn(PieceColor.BLACK), (4, 1))
        self.board.add_piece(Pawn(PieceColor.BLACK), (5, 1))
        self.board.add_piece(Pawn(PieceColor.BLACK), (6, 1))
        self.board.add_piece(Pawn(PieceColor.BLACK), (7, 1))

        self.board.add_piece(Rook(PieceColor.WHITE), (0, 7))
        self.board.add_piece(Rook(PieceColor.WHITE), (7, 7))

        self.board.add_piece(Rook(PieceColor.BLACK), (0, 0))
        self.board.add_piece(Rook(PieceColor.BLACK), (7, 0))

        self.board.add_piece(Knight(PieceColor.WHITE), (1, 7))
        self.board.add_piece(Knight(PieceColor.WHITE), (6, 7))

        self.board.add_piece(Knight(PieceColor.BLACK), (1, 0))
        self.board.add_piece(Knight(PieceColor.BLACK), (6, 0))

        self.board.add_piece(Bishop(PieceColor.WHITE), (2, 7))
        self.board.add_piece(Bishop(PieceColor.WHITE), (5, 7))

        self.board.add_piece(Bishop(PieceColor.BLACK), (2, 0))
        self.board.add_piece(Bishop(PieceColor.BLACK), (5, 0))

        self.board.add_piece(Queen(PieceColor.WHITE), (3, 7))
        self.board.add_piece(Queen(PieceColor.BLACK), (3, 0))

        self.board.add_piece(King(PieceColor.WHITE), (4, 7))
        self.board.add_piece(King(PieceColor.BLACK), (4, 0))

        self.running = True

    def loop(self):
        """Run the game loop"""
        while self.running:
            self.update()
            self.draw()

    def update(self):
        """Handle user events for each frame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.handle_click(event.pos)

    def draw(self):
        """Draw the game to the screen"""
        self.screen.fill((0, 0, 0))

        self.board.draw(self.screen)

        pygame.display.update()
        self.clock.tick(15)


if __name__ == '__main__':
    game = Game(600, 600)
    game.run()
