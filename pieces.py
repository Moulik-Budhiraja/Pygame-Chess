from constants import PieceColor, PieceType, PositionStuff
from board import Position, Piece
import os
import pygame
pygame.font.init()

# I'm not about to write doc strings for all of the classes,
# they all inherit from Piece


class Pawn(Piece):
    def __init__(self, color: PieceColor):

        if color == PieceColor.WHITE:
            image = pygame.image.load(os.path.join("images", "white_pawn.png"))
        else:
            image = pygame.image.load(os.path.join("images", "black_pawn.png"))

        image = pygame.transform.scale(
            image, (PositionStuff.PIECE_SIZE, PositionStuff.PIECE_SIZE))

        super().__init__(image, color)

        # Pawn specific
        self.double_moved = False
        self.type = PieceType.PAWN

    def get_moves(self, ignore_check: bool = False):
        if not ignore_check:
            if self.color != self.pos.board.move % 2:
                return []

        moves = []

        if self.color == PieceColor.WHITE:
            dir = 1
        else:
            dir = -1

            # Forward 1
        if self.pos.get_relative(0, -1 * dir).piece is None:
            moves.append(self.pos.get_relative(0, -1 * dir))

        # Forward 2
            if self.first_move:
                try:
                    if self.pos.get_relative(0, -2 * dir).piece is None:
                        moves.append(self.pos.get_relative(0, -2 * dir))
                except IndexError:
                    pass

        # Capture right
        try:
            if self.pos.get_relative(1, -1 * dir).piece is not None and \
                    self.pos.get_relative(1, -1 * dir).piece.color != self.color:
                moves.append(self.pos.get_relative(1, -1 * dir))
        except IndexError:
            pass

        # Capture left
        try:
            if self.pos.get_relative(-1, -1 * dir).piece is not None and \
                    self.pos.get_relative(-1, -1 * dir).piece.color != self.color:
                moves.append(self.pos.get_relative(-1, -1 * dir))
        except IndexError:
            pass

        # En passant right
        try:
            if self.pos.get_relative(1, 0).piece is not None and \
                self.pos.get_relative(1, 0).piece.color != self.color and \
                self.pos.get_relative(1, 0 * dir).piece.type == PieceType.PAWN and \
                self.pos.get_relative(1, 0 * dir).piece.double_moved and \
                    self.pos.get_relative(1, 0 * dir).piece.last_move_turn == self.pos.board.move - 1:
                moves.append(self.pos.get_relative(1, -1 * dir))
        except IndexError:
            pass

        # En passant left
        try:
            if self.pos.get_relative(-1, 0).piece is not None and \
                self.pos.get_relative(-1, 0).piece.color != self.color and \
                self.pos.get_relative(-1, 0 * dir).piece.type == PieceType.PAWN and \
                self.pos.get_relative(-1, 0 * dir).piece.double_moved and \
                    self.pos.get_relative(-1, 0 * dir).piece.last_move_turn == self.pos.board.move - 1:
                moves.append(self.pos.get_relative(-1, -1 * dir))
        except IndexError:
            pass

        if not ignore_check:
            moves = self.check_moves(moves)

        return moves

    def move(self, pos: Position):
        if self.color == PieceColor.WHITE:
            dir = 1
        else:
            dir = -1

        if self.first_move:
            if pos == self.pos.get_relative(0, -2 * dir):
                self.double_moved = True

        else:
            self.double_moved = False

        # Take piece on en passant

        if pos.piece is None:
            try:
                if self.pos.get_relative(1, -1 * dir) == pos:
                    self.pos.get_relative(1, 0).piece.take()
            except IndexError:
                pass

            try:

                if self.pos.get_relative(-1, -1 * dir) == pos:
                    self.pos.get_relative(-1, 0).piece.take()
            except IndexError:
                pass

        super().move(pos)


class Rook(Piece):
    def __init__(self, color: PieceColor):

        if color == PieceColor.WHITE:
            image = pygame.image.load(os.path.join("images", "white_rook.png"))
        else:
            image = pygame.image.load(os.path.join("images", "black_rook.png"))

        image = pygame.transform.scale(
            image, (PositionStuff.PIECE_SIZE, PositionStuff.PIECE_SIZE))

        super().__init__(image, color)

        # Rook specific
        self.type = PieceType.ROOK

    def get_moves(self, ignore_check: bool = False):
        if not ignore_check:
            if self.color != self.pos.board.move % 2:
                return []

        moves = []

        for i in range(1, 8):
            try:
                if self.pos.get_relative(0, i).piece is None or \
                        self.pos.get_relative(0, i).piece.color != self.color:
                    moves.append(self.pos.get_relative(0, i))

                    if self.pos.get_relative(0, i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(0, -i).piece is None or \
                        self.pos.get_relative(0, -i).piece.color != self.color:
                    moves.append(self.pos.get_relative(0, -i))

                    if self.pos.get_relative(0, -i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(i, 0).piece is None or \
                        self.pos.get_relative(i, 0).piece.color != self.color:
                    moves.append(self.pos.get_relative(i, 0))

                    if self.pos.get_relative(i, 0).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(-i, 0).piece is None or \
                        self.pos.get_relative(-i, 0).piece.color != self.color:
                    moves.append(self.pos.get_relative(-i, 0))

                    if self.pos.get_relative(-i, 0).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        if not ignore_check:
            moves = self.check_moves(moves)

        return moves


class Bishop(Piece):
    def __init__(self, color: PieceColor):

        if color == PieceColor.WHITE:
            image = pygame.image.load(
                os.path.join("images", "white_bishop.png"))
        else:
            image = pygame.image.load(
                os.path.join("images", "black_bishop.png"))

        image = pygame.transform.scale(
            image, (PositionStuff.PIECE_SIZE, PositionStuff.PIECE_SIZE))

        super().__init__(image, color)

        # Bishop specific
        self.type = PieceType.BISHOP

    def get_moves(self, ignore_check: bool = False):
        if not ignore_check:
            if self.color != self.pos.board.move % 2:
                return []

        moves = []

        for i in range(1, 8):
            try:
                if self.pos.get_relative(i, i).piece is None or \
                        self.pos.get_relative(i, i).piece.color != self.color:
                    moves.append(self.pos.get_relative(i, i))

                    if self.pos.get_relative(i, i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(-i, i).piece is None or \
                        self.pos.get_relative(-i, i).piece.color != self.color:
                    moves.append(self.pos.get_relative(-i, i))

                    if self.pos.get_relative(-i, i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(i, -i).piece is None or \
                        self.pos.get_relative(i, -i).piece.color != self.color:
                    moves.append(self.pos.get_relative(i, -i))

                    if self.pos.get_relative(i, -i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(-i, -i).piece is None or \
                        self.pos.get_relative(-i, -i).piece.color != self.color:
                    moves.append(self.pos.get_relative(-i, -i))

                    if self.pos.get_relative(-i, -i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        if not ignore_check:
            moves = self.check_moves(moves)

        return moves


class Queen(Piece):
    def __init__(self, color: PieceColor):

        if color == PieceColor.WHITE:
            image = pygame.image.load(
                os.path.join("images", "white_queen.png"))
        else:
            image = pygame.image.load(
                os.path.join("images", "black_queen.png"))

        image = pygame.transform.scale(
            image, (PositionStuff.PIECE_SIZE, PositionStuff.PIECE_SIZE))

        super().__init__(image, color)

        # Queen specific
        self.type = PieceType.QUEEN

    def get_moves(self, ignore_check: bool = False):
        if not ignore_check:
            if self.color != self.pos.board.move % 2:
                return []

        moves = []

        for i in range(1, 8):
            try:
                if self.pos.get_relative(0, i).piece is None or \
                        self.pos.get_relative(0, i).piece.color != self.color:
                    moves.append(self.pos.get_relative(0, i))

                    if self.pos.get_relative(0, i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(0, -i).piece is None or \
                        self.pos.get_relative(0, -i).piece.color != self.color:
                    moves.append(self.pos.get_relative(0, -i))

                    if self.pos.get_relative(0, -i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(i, 0).piece is None or \
                        self.pos.get_relative(i, 0).piece.color != self.color:
                    moves.append(self.pos.get_relative(i, 0))

                    if self.pos.get_relative(i, 0).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(-i, 0).piece is None or \
                        self.pos.get_relative(-i, 0).piece.color != self.color:
                    moves.append(self.pos.get_relative(-i, 0))

                    if self.pos.get_relative(-i, 0).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(i, i).piece is None or \
                        self.pos.get_relative(i, i).piece.color != self.color:
                    moves.append(self.pos.get_relative(i, i))

                    if self.pos.get_relative(i, i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(-i, i).piece is None or \
                        self.pos.get_relative(-i, i).piece.color != self.color:
                    moves.append(self.pos.get_relative(-i, i))

                    if self.pos.get_relative(-i, i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(i, -i).piece is None or \
                        self.pos.get_relative(i, -i).piece.color != self.color:
                    moves.append(self.pos.get_relative(i, -i))

                    if self.pos.get_relative(i, -i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                if self.pos.get_relative(-i, -i).piece is None or \
                        self.pos.get_relative(-i, -i).piece.color != self.color:
                    moves.append(self.pos.get_relative(-i, -i))

                    if self.pos.get_relative(-i, -i).piece is not None:
                        break
                else:
                    break
            except IndexError:
                break

        if not ignore_check:
            moves = self.check_moves(moves)

        return moves


class Knight(Piece):
    def __init__(self, color: PieceColor):

        if color == PieceColor.WHITE:
            image = pygame.image.load(
                os.path.join("images", "white_knight.png"))
        else:
            image = pygame.image.load(
                os.path.join("images", "black_knight.png"))

        image = pygame.transform.scale(
            image, (PositionStuff.PIECE_SIZE, PositionStuff.PIECE_SIZE))

        super().__init__(image, color)

        # Knight specific
        self.type = PieceType.KNIGHT

    def get_moves(self, ignore_check: bool = False):
        if not ignore_check:
            if self.color != self.pos.board.move % 2:
                return []

        moves = []

        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if abs(i) == abs(j):
                    continue

                try:
                    if self.pos.get_relative(i, j).piece is None or \
                            self.pos.get_relative(i, j).piece.color != self.color:
                        moves.append(self.pos.get_relative(i, j))
                except IndexError:
                    continue

        if not ignore_check:
            moves = self.check_moves(moves)

        return moves


class King(Piece):
    def __init__(self, color: PieceColor):

        if color == PieceColor.WHITE:
            image = pygame.image.load(
                os.path.join("images", "white_king.png"))
        else:
            image = pygame.image.load(
                os.path.join("images", "black_king.png"))

        image = pygame.transform.scale(
            image, (PositionStuff.PIECE_SIZE, PositionStuff.PIECE_SIZE))

        super().__init__(image, color)

        # King specific
        self.type = PieceType.KING
        self.in_check = False
        self.checkmate = False

    def get_moves(self, ignore_check: bool = False):
        if not ignore_check:
            if self.color != self.pos.board.move % 2:
                return []

        moves = []

        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                if i == 0 and j == 0:
                    continue

                try:
                    if self.pos.get_relative(i, j).piece is None or \
                            self.pos.get_relative(i, j).piece.color != self.color:
                        moves.append(self.pos.get_relative(i, j))
                except IndexError:
                    continue

        # Castling
        if self.first_move and not self.in_check:
            if self.color == PieceColor.WHITE:
                if self.pos.get_relative(1, 0).piece is None and \
                        self.pos.get_relative(2, 0).piece is None and \
                        self.pos.get_relative(3, 0).piece is not None and \
                        self.pos.get_relative(3, 0).piece.type == PieceType.ROOK and \
                        self.pos.get_relative(3, 0).piece.first_move:
                    moves.append(self.pos.get_relative(2, 0))

                if self.pos.get_relative(-1, 0).piece is None and \
                        self.pos.get_relative(-2, 0).piece is None and \
                        self.pos.get_relative(-3, 0).piece is None and \
                        self.pos.get_relative(-4, 0).piece is not None and \
                        self.pos.get_relative(-4, 0).piece.type == PieceType.ROOK and \
                        self.pos.get_relative(-4, 0).piece.first_move:
                    moves.append(self.pos.get_relative(-2, 0))

        if not ignore_check:
            original_pos = self.pos

            if self.color == PieceColor.WHITE:
                opponent_pieces = Piece.black_pieces
            else:
                opponent_pieces = Piece.white_pieces

            valid_moves = []

            self.pos.piece = None

            for pos in moves:
                original_piece = pos.piece
                self.pos = pos

                opponent_moves = []

                for piece in opponent_pieces:
                    opponent_moves += piece.get_moves(ignore_check=True)

                if self.pos in opponent_moves:
                    self.pos.piece = original_piece
                    continue

                valid_moves.append(self.pos)

                self.pos.piece = original_piece

            self.pos = original_pos

            return valid_moves

        return moves

    def check_checked(self):
        """Checks if the king is in check"""
        if self.color == PieceColor.WHITE:
            opponent_pieces = Piece.black_pieces
        else:
            opponent_pieces = Piece.white_pieces

        opponent_moves = []

        for piece in opponent_pieces:
            opponent_moves += piece.get_moves(ignore_check=True)

        if self.pos in opponent_moves:
            self.in_check = True
        else:
            self.in_check = False

    def check_checkmate(self):
        """Checks if the king is in checkmate or stalemate"""
        # Check all possible moves for the color to prevent checkmate
        if self.color == PieceColor.WHITE:
            opponent_pieces = Piece.black_pieces[:]
            own_pieces = Piece.white_pieces[:]
        else:
            opponent_pieces = Piece.white_pieces[:]
            own_pieces = Piece.black_pieces[:]

        own_moves = []

        for piece in own_pieces:
            original_pos = piece.pos
            if piece.type == PieceType.KING:
                piece_moves = piece.get_moves()
                own_moves += piece_moves
                continue
            else:
                piece_moves = piece.get_moves(ignore_check=True)

            for pos in piece_moves:
                original_piece = pos.piece

                if original_piece != None and original_piece.color != self.color:
                    opponent_pieces.remove(original_piece)

                pos.piece = piece

                opponent_moves = []

                for opponent_piece in opponent_pieces:
                    opponent_moves += opponent_piece.get_moves(
                        ignore_check=True)

                if original_piece != None and original_piece.color != self.color:
                    opponent_pieces.append(original_piece)

                if self.pos in opponent_moves:
                    pos.piece = original_piece
                    continue

                own_moves.append(pos)

                pos.piece = original_piece

            piece.pos = original_pos

        if len(own_moves) == 0:
            self.checkmate = True

    def move(self, pos: Position):
        if pos == self.pos.get_relative(-2, 0):
            rook = self.pos.get_relative(-4, 0)
            rook.move(self.pos.get_relative(-1, 0))

        if pos == self.pos.get_relative(2, 0):
            rook = self.pos.get_relative(3, 0)
            rook.move(self.pos.get_relative(1, 0))

        super().move(pos)
