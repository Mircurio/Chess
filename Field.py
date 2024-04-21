import  pygame
from figures import *

class CellDontContainsPiece(Exception):

    def __init__(self, message = "Cell don't contains piece"):
        super().__init__(message)

class Cell:

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__piece = None

    def getPiece(self):
        if self.__piece != None:
            return self.__piece
        else:
            raise CellDontContainsPiece()

    def __getCenter(self):
        return (self.__x2 + self.__x1) / 2, (self.__y2 + self.__y1) / 2

    def setPiece(self, piece: ChessPiece):
        self.__piece = piece
        center = self.__getCenter()
        piece.setСoordinates(center[0], center[1])

    def delPiece(self):
        self.__piece = None

class Field:

    def __init__(self, filename):
        self.__cells = []

        # Рвзмер поля в длину и ширину (В клетках).
        fieldSize = 8

        #Заполнение пустыми списками.
        for i in range(fieldSize):
            self.__cells.append(list())

        self.__image = pygame.image.load(filename).convert_alpha()

        # Координаты левой верхней клетки.
        firstCellX1 = 83
        firstCellY1 = 83
        firstCellx2 = 168
        firstCellY2 = 166

        deltaX = firstCellx2 - firstCellX1
        deltaY = firstCellY2 - firstCellY1
        deltaScreen = -26
        for rowNumber in range(fieldSize):


            for columnNumber in range(fieldSize):
                self.__cells[rowNumber].append(
                     Cell(firstCellX1 + deltaX * columnNumber + deltaScreen, firstCellY1 + firstCellY1 * rowNumber,
                           firstCellx2 + firstCellx2 * columnNumber + deltaScreen, firstCellY2 + firstCellY2 * rowNumber))

    def getImage(self):
        return self.__image

    def addPiece(self, cellRowIndex, cellColumnIndex, piece: ChessPiece):
        self.__cells[cellRowIndex][cellColumnIndex].setPiece(piece)

    def getPiece(self, cellRowIndex, cellColumnIndex):
        return  self.__cells[cellRowIndex][cellColumnIndex].getPiece()
