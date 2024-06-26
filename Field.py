import copy

import  pygame
from figures import *

class CellDontContainsPiece(Exception):

    def __init__(self, message = "Cell don't contains piece"):
        super().__init__(message)

class CannotFindThisCell(Exception):

    def __init__(self, message = "Can't find this cell!"):
        super().__init__(message)

class WrongTeam(Exception):

    def __init__(self, message = "Wrong team!"):
        super().__init__(message)

class Cell:

    def __init__(self, x1, y1, x2, y2, row, column):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__piece = None
        self.__isSelected = False
        self.__row = row
        self.__column = column

    def getPiece(self):
        if self.__piece != None:
            return self.__piece
        else:
            raise CellDontContainsPiece()

    def __getCenter(self):
        return (self.__x2 + self.__x1) / 2, (self.__y2 + self.__y1) / 2

    def setPiece(self, piece : ChessPiece):
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

    def isEmpty(self):
        if self.__piece == None:
            return True
        else:
            return False

    def getRow(self):
        return self.__row

    def getColumn(self):
        return self.__column

class Field:

    __fieldSize = 8

    def __init__(self):
        self.__cells = []

        # Рвзмер поля в длину и ширину (В клетках).

        #Заполнение пустыми списками.
        for i in range(self.__fieldSize):
            self.__cells.append(list())

        # Координаты левой верхней клетки.
        firstCellX1 = 180
        firstCellY1 = 88
        firstCellx2 = 266
        firstCellY2 = 171

        deltaX = firstCellx2 - firstCellX1
        deltaY = firstCellY2 - firstCellY1
        for rowNumber in range(self.__fieldSize):


            for columnNumber in range(self.__fieldSize):
                self.__cells[rowNumber].append(
                     Cell(firstCellX1 + deltaX * columnNumber, firstCellY1 + deltaY * rowNumber,
                           firstCellx2 + deltaX * columnNumber, firstCellY2 + deltaY * rowNumber, rowNumber, columnNumber))

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


    def getCell(self, row, column):
        fieldSize = 8

        if row >= fieldSize or row < 0 or column >= fieldSize or column < 0:
            raise IndexError

        return self.__cells[row][column]

    def addPiece(self, cellRowIndex, cellColumnIndex, piece: ChessPiece):
        self.__cells[cellRowIndex][cellColumnIndex].setPiece(piece)

    def getPiece(self, cellRowIndex, cellColumnIndex):
        return  self.__cells[cellRowIndex][cellColumnIndex].getPiece()

    def getFieldSize(self):
        return self.__fieldSize

    def moveFigure(self, moveFrom, moveTo, returnBack = False):
        '''
        Двигает фигуры на доске, если это правомерно. Возвращает в слечае успеха True, иначе - False.
        Необязательный параметр returnBack возвращает фигуры обратно, если равен True (по умолчанию False).
        '''

        if moveFrom.getPiece().canMove(self, moveFrom, moveTo):

            moveFromPiece = moveFrom.getPiece()

            moveToIsEmpty = False

            try:
                moveToPiece = moveTo.getPiece()
            except CellDontContainsPiece:
                moveToPiece = None
                moveToIsEmpty = True

            moveTo.setPiece(moveFrom.getPiece())

            moveFrom.delPiece()
            team = moveFromPiece.getTeam()

            kingCell = self.findKingCell(team)

            if kingCell.getPiece().isUnderAttack(self, kingCell):

                moveFrom.setPiece(moveFromPiece)

                if not moveToIsEmpty:
                    moveTo.setPiece(moveToPiece)
                else:
                    moveTo.delPiece()

                return False

            if returnBack:
                moveFrom.setPiece(moveFromPiece)

                if not moveToIsEmpty:
                    moveTo.setPiece(moveToPiece)
                else:
                    moveTo.delPiece()

            return True

        return False

    def getWinnerOrNone(self):
        '''Возвращает победившую команду(строку) или None, если таковой нет.'''

        whiteKingCell = self.findKingCell("white")
        blackKingCell = self.findKingCell("black")

        if whiteKingCell.getPiece().isCheckmated(self, whiteKingCell):
            return "black"
        elif blackKingCell.getPiece().isCheckmated(self, blackKingCell):
            return "white"
        else:
            return None


    def findKingCell(self, team: str):
        '''Возвращает клетку, в которой находится король. Короля нельзя съесть, поэтому он всегда будет на поле.'''

        if team != "white" and team != "black":
            raise WrongTeam()

        for row in range(self.__fieldSize):
            for column in range(self.__fieldSize):

                try:

                    piece = self.getPiece(row, column)
                    if type(piece) == King and piece.getTeam() == team:
                        return self.getCell(row, column)

                except CellDontContainsPiece:
                    pass


    def findCell(self, coordinates):
        '''Возвращяет клетку, внутри которой находятся данные координаты. В противном случае - выбрасывает исключение.'''

        x, y = coordinates

        fieldSize = 8
        for rowNumber in range(fieldSize):
            for columnNumber in range(fieldSize):

                x1, y1, x2, y2 = self.__cells[rowNumber][columnNumber].getCoordinates()
                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    return self.__cells[rowNumber][columnNumber]

        raise CannotFindThisCell()

    def blitAllPieces(self, screen):
        '''Выводит все шахматные фигуры на экран.'''

        for row in self.__cells:
            for cell in row:

                #Если клетка не содержит фигуру, то просто пропускаем её.
                try:
                    screen.blit(cell.getPiece().getImage(), cell.getPiece().getRect())
                except CellDontContainsPiece:
                    pass
