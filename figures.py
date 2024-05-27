import pygame

class ImageIsNone(Exception):
    def __init__(self, message = "Image is none."):
        super().__init__(message)

class ChessPiece(pygame.sprite.Sprite):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__()
        self.__team = team
        self.__image = pygame.image.load(filename).convert_alpha()

        if (x != None) and (y != None):
            self.__rect = self.__image.get_rect(center = (x, y))
        else:
            self.__rect = None

    def setСoordinates(self, x, y):
        self.__rect = self.__image.get_rect(center=(x, y))

    def getImage(self):

        if (self.__image != None):
            return self.__image
        else:
            raise ImageIsNone()

    def getRect(self):
        return self.__rect

class Queen(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

class Bishop(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

class Rook(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)


class Knight(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

class Pawn(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

class King(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)