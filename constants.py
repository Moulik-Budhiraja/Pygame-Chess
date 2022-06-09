class Colors:
    """All colors the might be used in the game"""
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)
    ORANGE = (255, 165, 0)
    BROWN = (165, 42, 42)
    LIGHT_BLUE = (0, 191, 255)
    LIGHT_GREEN = (144, 238, 144)
    LIGHT_RED = (255, 182, 193)
    LIGHT_PURPLE = (255, 20, 147)
    LIGHT_CYAN = (0, 255, 255)
    LIGHT_ORANGE = (255, 140, 0)
    LIGHT_BROWN = (210, 180, 140)
    DARK_BLUE = (0, 0, 139)
    DARK_GREEN = (0, 100, 0)
    DARK_RED = (139, 0, 0)
    DARK_PURPLE = (128, 0, 128)
    DARK_CYAN = (0, 139, 139)
    DARK_ORANGE = (255, 140, 0)
    DARK_BROWN = (165, 42, 42)
    LIGHT_GRAY = (211, 211, 211)
    DARK_GRAY = (169, 169, 169)
    GRAY = (128, 128, 128)
    DARK_GRAY2 = (64, 64, 64)
    LIGHT_GRAY2 = (192, 192, 192)
    DARK_GRAY3 = (105, 105, 105)
    LIGHT_GRAY3 = (205, 205, 205)


class TransparentColors:
    """All transparent colors the might be used in the game"""
    GREEN = (0, 255, 0, 128)
    RED = (255, 0, 0, 128)
    BLUE = (0, 0, 255, 128)
    BLACK = (0, 0, 0, 128)
    WHITE = (255, 255, 255, 128)
    YELLOW = (255, 255, 0, 128)
    PURPLE = (255, 0, 255, 128)
    CYAN = (0, 255, 255, 128)
    ORANGE = (255, 165, 0, 128)
    BROWN = (165, 42, 42, 128)
    LIGHT_BLUE = (0, 191, 255, 128)
    LIGHT_GREEN = (144, 238, 144, 128)
    LIGHT_RED = (255, 182, 193, 128)
    LIGHT_PURPLE = (255, 20, 147, 128)
    LIGHT_CYAN = (0, 255, 255, 128)
    LIGHT_ORANGE = (255, 140, 0, 128)
    LIGHT_BROWN = (210, 180, 140, 128)
    DARK_BLUE = (0, 0, 139, 128)
    DARK_GREEN = (0, 100, 0, 128)
    DARK_RED = (139, 0, 0, 128)
    DARK_PURPLE = (128, 0, 128, 128)
    DARK_CYAN = (0, 139, 139, 128)
    DARK_ORANGE = (255, 140, 0, 128)
    DARK_BROWN = (165, 42, 42, 128)
    LIGHT_GRAY = (211, 211, 211, 128)
    DARK_GRAY = (169, 169, 169, 128)
    GRAY = (128, 128, 128, 128)
    DARK_GRAY2 = (64, 64, 64, 128)
    LIGHT_GRAY2 = (192, 192, 192, 128)
    DARK_GRAY3 = (105, 105, 105, 128)
    LIGHT_GRAY3 = (205, 205, 205, 128)
    DARK_GRAY4 = (51, 51, 51, 128)
    LIGHT_GRAY4 = (153, 153, 153, 128)
    DARK_GRAY5 = (25, 25, 25, 128)
    LIGHT_GRAY5 = (76, 76, 76, 128)


class PieceColor:
    """The color of a piece"""
    WHITE = 0
    BLACK = 1


class PieceType:
    """The type of piece"""
    PAWN = "PAWN"
    KNIGHT = "KNIGHT"
    BISHOP = "BISHOP"
    ROOK = "ROOK"
    QUEEN = "QUEEN"
    KING = "KING"


class PositionStuff:
    """Don't judge couldn't come up with a better name"""
    PIECE_SIZE = 60
