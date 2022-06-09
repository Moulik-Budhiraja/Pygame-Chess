from turtle import position
import pygame
from constants import Colors, TransparentColors, PieceColor, PieceType
import random


class Board:
    """The board for the game. Stores positions and king pieces."""

    def __init__(self, x: int, y: int, size: int):
        self.x = x
        self.y = y
        self.size = size // 8 * 8  # Rounds to the nearest multiple of 8

        self.screen = pygame.Surface((self.size, self.size))

        self.board = [[Position(x, y, self.size // 8, self)
                       for x in range(8)] for y in range(8)]

        self.selected_pos = None

        self.move = 0

        self.white_king = None
        self.black_king = None

    @property
    def selected_pos(self):
        """Stores which position is selected."""
        return self._selected_pos

    @selected_pos.setter
    def selected_pos(self, pos: 'Position'):

        try:
            if self._selected_pos is not None:
                self._selected_pos.selected = False
        except AttributeError:
            self._selected_pos = None
            return

        if pos is None:
            self._selected_pos = None
            return

        self._selected_pos = pos
        self._selected_pos.selected = True

    def __index__(self, index):
        return self.board[index]

    def __iter__(self):
        return iter(self.board)

    def draw(self, screen: pygame.Surface):
        """Draw the board and all pieces"""
        for row in self.board:
            for position in row:
                position.draw(self.screen)

        screen.blit(self.screen, (self.x, self.y))

    def handle_click(self, pos: tuple):
        """Send the click to the selected position."""
        x, y = pos
        x -= self.x
        y -= self.y

        # If click is out of bounds, return
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            return

        x = x // (self.size // 8)
        y = y // (self.size // 8)

        self.board[y][x].handle_click()

    def add_piece(self, piece: 'Piece', pos: tuple):
        """Link a piece to a position on the board."""
        x, y = pos
        piece.pos = self.board[y][x]

        if piece.type == PieceType.KING:
            if piece.color == PieceColor.WHITE:
                self.white_king = piece
            else:
                self.black_king = piece

    def check_checked(self):
        """Check if either king is in check."""
        if not self.black_king is None:
            self.black_king.check_checked()

        if not self.white_king is None:
            self.white_king.check_checked()

        self.check_checkmate()

    def check_checkmate(self):
        """Check if either king is in checkmate."""
        if not self.black_king is None:
            self.black_king.check_checkmate()

        if not self.white_king is None:
            self.white_king.check_checkmate()


class Position:
    """Represents a square on the board."""

    def __init__(self, x: int, y: int, size: int, board: Board):
        self.x = x
        self.y = y
        self.size = size
        self.board = board

        self.selected = False
        self.hovered = False

        self.piece = None

    @property
    def rect(self):
        return pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def __eq__(self, other: 'Position'):
        return self.x == other.x and self.y == other.y

    def draw(self, screen: pygame.Surface):
        """Draw the position with its piece and highlight."""
        # Check white or black
        if self.x % 2 == self.y % 2:
            color = Colors.WHITE
        else:
            color = Colors.DARK_GRAY

        # Draw the square
        pygame.draw.rect(screen, color, self.rect)

        if self.selected:
            # Draw partially transparent square
            surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
            surface.fill(TransparentColors.YELLOW)
            screen.blit(surface, self.rect)

            if self.piece is not None:
                for pos in self.piece.get_moves():
                    pos.hovered = True

        if self.hovered:
            if self.piece is None:
                surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
                surface.fill(TransparentColors.BLUE)
                screen.blit(surface, self.rect)
            else:
                surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
                surface.fill(TransparentColors.RED)
                screen.blit(surface, self.rect)

        if self.piece is not None:
            if self.piece.type == PieceType.KING:
                if self.piece.in_check and not self.piece.checkmate:
                    surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
                    surface.fill(TransparentColors.DARK_RED)
                    screen.blit(surface, self.rect)
                elif self.piece.checkmate:
                    surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
                    surface.fill(TransparentColors.DARK_GRAY5)
                    screen.blit(surface, self.rect)

            # Draw piece in the center of the square
            screen.blit(self.piece.image, (self.rect.centerx - self.piece.image.get_width() //
                        2, self.rect.centery - self.piece.image.get_height() // 2))

        self.hovered = False

    def handle_click(self):
        """Handle a click on the position."""
        if self.piece is None:
            if self.board.selected_pos is None:
                if self.selected:
                    self.board.selected_pos = None
                else:
                    self.board.selected_pos = self
                return
            elif self in self.board.selected_pos.get_moves():
                self.board.selected_pos.move(self)
                self.board.selected_pos = None
                return
            else:
                if self.selected:
                    self.board.selected_pos = None
                else:
                    self.board.selected_pos = self
        else:
            if self.board.selected_pos is None:
                self.board.selected_pos = self
                return
            elif self in self.board.selected_pos.get_moves():
                self.board.selected_pos.move(self)
                self.board.selected_pos = None
                return
            else:
                if self.selected:
                    self.board.selected_pos = None
                else:
                    self.board.selected_pos = self

    def get_moves(self):
        """Get all possible moves for the piece at this position."""
        if self.piece is None:
            return []
        return self.piece.get_moves()

    def move(self, pos: 'Position'):
        """Move the piece to a new position."""
        if self.piece == None:
            raise ValueError("No piece to move")

        self.piece.move(pos)

        self.board.move += 1

    def get_relative(self, x_offset, y_offset):
        """Get the position relative to this one."""
        new_x = self.x + x_offset
        new_y = self.y + y_offset

        if new_x < 0 or new_y < 0 or new_x >= 8 or new_y >= 8:
            raise IndexError("Position is out of bounds")

        return self.board.board[new_y][new_x]


class Piece:
    """Represents a piece on the board."""
    black_pieces = []
    white_pieces = []

    def __init__(self, image: pygame.Surface, color: PieceColor):
        self.image = image

        self.first_move = True
        self.last_move_turn = 0

        self.color = color

        self.type = None

        # Add this piece to the public list of pieces
        if color == PieceColor.BLACK:
            Piece.black_pieces.append(self)
        else:
            Piece.white_pieces.append(self)

    def __repr__(self):
        return f"Piece({'WHITE' if self.color == 0 else 'BLACK'} {self.type} at {self.pos})"

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value: Position):
        self._pos = value
        if not value is None:
            self._pos.piece = self

    @property
    def rect(self):
        return self.image.get_rect()

    def get_moves(self):
        """Returns all possible moves for the piece"""
        return []

    def move(self, pos: Position):
        """Move the piece to a new position."""
        if pos.piece is not None:
            pos.piece.take()

        self.pos.piece = None
        self.pos = pos
        self.pos.piece = self

        self.first_move = False

        self.last_move_turn = self.pos.board.move

        self.pos.board.check_checked()

    def take(self):
        """Removes itself from the board"""
        self.pos.piece = None
        if self.color == PieceColor.WHITE:
            Piece.white_pieces.remove(self)
        else:
            Piece.black_pieces.remove(self)

    def check_moves(self, moves: list):
        """Checks if the king will be in check after the move"""
        if self.color == PieceColor.WHITE:
            king = self.pos.board.white_king
            opponent_pieces = Piece.black_pieces[:]
        else:
            king = self.pos.board.black_king
            opponent_pieces = Piece.white_pieces[:]

        valid_moves = []

        original_pos = self.pos
        self.pos.piece = None

        for pos in moves:
            original_piece = pos.piece
            self.pos = pos

            opponent_moves = []

            if original_piece is not None and original_piece.color != self.color:
                opponent_pieces.remove(original_piece)

            for piece in opponent_pieces:
                opponent_moves += piece.get_moves(ignore_check=True)

            if original_piece is not None and original_piece.color != self.color:
                opponent_pieces.append(original_piece)

            if not king.pos in opponent_moves:
                valid_moves.append(pos)

            pos.piece = original_piece

        self.pos = original_pos

        return valid_moves
