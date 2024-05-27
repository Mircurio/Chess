import  pygame
from figures import *

class CellDontContainsPiece(Exception):

    def __init__(self, message = "Cell don't contains piece"):
        super().__init__(message)

class CannotFindThisCell(Exception):

    def __init__(self, message = "Can't find this cell!"):
        super().__init__(message)

class Cell:

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__piece = None
        self.__isSelected = False

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

    def getCoordinates(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)

    def select(self):
        if self.__isSelected:
            self.__isSelected = False
        else:
            self.__isSelected = True

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
        firstCellX1 = 180
        firstCellY1 = 88
        firstCellx2 = 266
        firstCellY2 = 171

        deltaX = firstCellx2 - firstCellX1
        deltaY = firstCellY2 - firstCellY1
        for rowNumber in range(fieldSize):


            for columnNumber in range(fieldSize):
                self.__cells[rowNumber].append(
                     Cell(firstCellX1 + deltaX * columnNumber, firstCellY1 + deltaY * rowNumber,
                           firstCellx2 + deltaX * columnNumber, firstCellY2 + deltaY * rowNumber))

        imagesFolder = "Images"

        #Расставляем черные фигуры!
        self.addPiece(0, 3, Queen(imagesFolder + '\Chessmen\Black\Queen.png', "black"))
        self.addPiece(0, 0, Rook(imagesFolder + '\Chessmen\Black\Rook.png', "black"))
        self.addPiece(0, 7, Rook(imagesFolder + '\Chessmen\Black\Rook.png', "black"))
        self.addPiece(0, 2, Bishop(imagesFolder + '\Chessmen\Black\Bishop.png', "black"))
        self.addPiece(0, 5, Bishop(imagesFolder + '\Chessmen\Black\Bishop.png', "black"))
        self.addPiece(0, 1, Knight(imagesFolder + '\Chessmen\Black\Knight.png', "black"))
        self.addPiece(0, 6, Knight(imagesFolder + '\Chessmen\Black\Knight.png', "black"))
        self.addPiece(0, 4, King(imagesFolder + '\Chessmen\Black\King.png', "black"))

        #Добавляем 8 чёрных и белых пешек!
        for i in range(8):
            self.addPiece(1, i, Pawn(imagesFolder + '\Chessmen\Black\Pawn.png', "black"))
            self.addPiece(6, i, Pawn(imagesFolder + '\Chessmen\White\Pawn.png', "white"))


        # Расставляем белые фигуры!
        self.addPiece(7, 3, Queen(imagesFolder + '\Chessmen\White\Queen.png', "white"))
        self.addPiece(7, 0, Rook(imagesFolder + '\Chessmen\White\Rook.png', "white"))
        self.addPiece(7, 7, Rook(imagesFolder + '\Chessmen\White\Rook.png', "white"))
        self.addPiece(7, 2, Bishop(imagesFolder + '\Chessmen\White\Bishop.png', "white"))
        self.addPiece(7, 5, Bishop(imagesFolder + '\Chessmen\White\Bishop.png', "white"))
        self.addPiece(7, 1, Knight(imagesFolder + '\Chessmen\White\Knight.png', "white"))
        self.addPiece(7, 6, Knight(imagesFolder + '\Chessmen\White\Knight.png', "white"))
        self.addPiece(7, 4, King(imagesFolder + '\Chessmen\White\King.png', "white"))



    def getImage(self):
        return self.__image

    def addPiece(self, cellRowIndex, cellColumnIndex, piece: ChessPiece):
        self.__cells[cellRowIndex][cellColumnIndex].setPiece(piece)

    def getPiece(self, cellRowIndex, cellColumnIndex):
        return  self.__cells[cellRowIndex][cellColumnIndex].getPiece()

    def findCell(self, coordinates):
        '''Возвращяет клетку и её индекс, внутри которой находятся данные координаты. В противном случае - выбрасывает исключение.'''

        x, y = coordinates

        fieldSize = 8
        for rowNumber in range(fieldSize):
            for columnNumber in range(fieldSize):

                x1, y1, x2, y2 = self.__cells[rowNumber][columnNumber].getCoordinates()
                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    return self.__cells[rowNumber][columnNumber], rowNumber, columnNumber

        raise CannotFindThisCell()

    def blitAllPieces(self, screen):
        '''Выводит все шахматные фигуры на экран.'''

        for row in self.__cells:
            for cell in row:

                #Если клетка не содержит фигуру, то просто пропускаем её.
                try:
                    screen.blit(cell.getPiece().getImage(), cell.getPiece().getRect())
                except:
                    pass
