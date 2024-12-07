import pygame

class ImageIsNone(Exception):
    def __init__(self, message = "Image is none."):
        super().__init__(message)

class ChessPiece(pygame.sprite.Sprite):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__()
        self._team = team
        self._image = pygame.image.load(filename).convert_alpha()

        if (x != None) and (y != None):
            self.__rect = self._image.get_rect(center = (x, y))
        else:
            self.__rect = None

    def setСoordinates(self, x, y):
        self.__rect = self._image.get_rect(center=(x, y))

    def getImage(self):

        if (self._image != None):
            return self._image
        else:
            raise ImageIsNone()

    def getRect(self):
        return self.__rect

    def getTeam(self):
        return self._team


    # Ниже идут проверки.

    def _checkInfiniteDirection(self, field, currentCell, startCell, moveTo, deltaRow, deltaColumn):
        '''Функция проверяет в заданном бесконечном направлении(пока не вылезет исключение), можно ли пойти в эту клетку.'''

        # Нельзя есть через другие фигуры!
        if not currentCell.isEmpty() and currentCell is not moveTo and currentCell is not startCell:
            return False


        if currentCell is moveTo: # and not currentCell.isEmpty():
            if currentCell.isEmpty():
                return True
            elif currentCell.getPiece().getTeam() != self._team:
                return True
            else:
                return False

        return self._checkInfiniteDirection(field, field.getCell(currentCell.getRow() + deltaRow, currentCell.getColumn() + deltaColumn), startCell, moveTo, deltaRow, deltaColumn)



    def _checkDiagonal(self, field, moveFrom, moveTo):
        '''Рекурсивный алгоритм. Определяет, может ли фигура пойти по диагоналям во все стороны.'''

        directions = ((1, 1), (1, -1), (-1, 1), (-1, -1))

        for direction in directions:
            try:
                if self._checkInfiniteDirection(field, moveFrom, moveFrom, moveTo, direction[0], direction[1]):
                    return True
            except IndexError:
                pass

        return False


    def _checkStraight(self, field, moveFrom, moveTo):
        '''Рекурсивный алгоритм. Определяет, может ли фигура пойти по прямым во все стороны.'''

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for direction in directions:
            try:
                if self._checkInfiniteDirection(field, moveFrom, moveFrom, moveTo, direction[0], direction[1]):
                    return True
            except IndexError:
                pass

        return False


class Queen(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

    def canMove(self, field, moveFrom, moveTo):
        '''Возвращает True если фигура может пойти в эту клетку, иначе - False.'''

        if self._checkDiagonal(field, moveFrom, moveTo):
            return True
        elif self._checkStraight(field, moveFrom, moveTo):
            return True
        else:
            return False



class Bishop(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

    def canMove(self, field, moveFrom, moveTo):
        '''Возвращает True если фигура может пойти в эту клетку, иначе - False.'''

        if self._checkDiagonal(field, moveFrom, moveTo):
            return True
        else:
            return False

class Rook(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

    def canMove(self, field, moveFrom, moveTo):
        '''Возвращает True если фигура может пойти в эту клетку, иначе - False.'''

        if self._checkStraight(field, moveFrom, moveTo):
            return True
        else:
            return False


class Knight(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

    def canMove(self, field, moveFrom, moveTo):
        #Ходим буквой "Г".

        deltas = ((-2, -1), (-2,  1),
                  (-1,  2), (1,  2),
                  (2,  1), (2, -1),
                  (1, -2), (-1, -2))

        for delta in deltas:
            try:

                destinationCell = field.getCell(moveFrom.getRow() + delta[0], moveFrom.getColumn() + delta[1])
                if ((not destinationCell.isEmpty() and  destinationCell.getPiece().getTeam() != self._team) or (destinationCell.isEmpty())) and \
                    destinationCell is moveTo:
                    return True

            except IndexError:
                pass

        return False


class Pawn(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

    def canMove(self, field, moveFrom, moveTo):

        # Первый ходможет быть на две клетки.
        canMoveTwoCells = False
        if moveFrom.getRow() == 6 and self._team == "white":
            canMoveTwoCells = True
        elif moveFrom.getRow() == 1 and self._team == "black":
            canMoveTwoCells = True

        if self._team == "white":

            try:
                # Верхняя клетка должна быть пуста.
                topCell = field.getCell(moveFrom.getRow() - 1, moveFrom.getColumn())
                if topCell.isEmpty() and topCell is moveTo:
                    return True
            except:
                pass

            try:
                topTwoCell = field.getCell(moveFrom.getRow() - 2, moveFrom.getColumn())
                topCell = field.getCell(moveFrom.getRow() - 1, moveFrom.getColumn())
                if canMoveTwoCells and topCell.isEmpty() and topTwoCell.isEmpty() and topTwoCell is moveTo:
                    return True
            except:
                pass

            try:
                # Определяем возможность есть наискосок.
                topLeftCell = field.getCell(moveFrom.getRow() - 1, moveFrom.getColumn() - 1)
                if not topLeftCell.isEmpty() and topLeftCell is moveTo:
                    return True
            except:
                pass

            try:
                topRightCell = field.getCell(moveFrom.getRow() - 1, moveFrom.getColumn() + 1)
                if not topRightCell.isEmpty() and topRightCell is moveTo:
                    return True
            except:
                pass

            return False

        else:

            try:
                bottomCell = field.getCell(moveFrom.getRow() + 1, moveFrom.getColumn())
                if bottomCell.isEmpty() and bottomCell is moveTo:
                    return True
            except:
                pass

            try:
                topTwoCell = field.getCell(moveFrom.getRow() + 2, moveFrom.getColumn())
                topCell = field.getCell(moveFrom.getRow() + 1, moveFrom.getColumn())
                if canMoveTwoCells and topCell.isEmpty() and topTwoCell.isEmpty() and topTwoCell is moveTo:
                    return True
            except:
                pass

            try:
                bottomLeftCell = field.getCell(moveFrom.getRow() + 1, moveFrom.getColumn() - 1)
                if not bottomLeftCell.isEmpty() and bottomLeftCell is moveTo:
                    return True
            except:
                pass

            try:
                BottomRightCell = field.getCell(moveFrom.getRow() + 1, moveFrom.getColumn() + 1)
                if not BottomRightCell.isEmpty() and BottomRightCell is moveTo:
                    return True
            except:
                pass

            return False


class King(ChessPiece):

    def __init__(self, filename, team, x = None, y = None):
        super().__init__(filename, team, x, y)

    def isUnderAttack(self, field, kingCell):
        '''Атакован ли король?'''

        fieldSize = field.getFieldSize()

        for row in range(fieldSize):
            for column in range(fieldSize):
                try:
                    cell = field.getCell(row, column)

                    if cell.getPiece().getTeam() != self._team and cell.getPiece().canMove(field, cell, kingCell):
                        return True
                except:
                    pass

        return False


    def isCheckmated(self, field, kingCell):
        '''Возвращает True, если королю поставлен мат, иначе - False.'''

        if self.isUnderAttack(field, kingCell):
            deltaCells = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

            for deltaCell in deltaCells:

                try:
                    nearCell = field.getCell(kingCell.getRow() + deltaCell[0], kingCell.getColumn() + deltaCell[1])

                    if nearCell.isEmpty() :
                        # Если на соседней клетке король не атакован - значит это не мат.
                        if not self.isUnderAttack(field, nearCell):
                            return False
                except:
                    pass

            # Если король не может уйти от шаха, то проверяем, может ли другая фигура закрыть его.
            fieldSize = field.getFieldSize()

            for row in range(fieldSize):
                for column in range(fieldSize):

                    moveFrom = field.getCell(row, column)

                    for row2 in range(fieldSize):
                        for column2 in range(fieldSize):
                            moveTo = field.getCell(row2, column2)

                            try:
                                if moveFrom.getPiece().getTeam() == self._team and (moveTo.isEmpty() or moveTo.getPiece().getTeam != self._team)\
                                        and field.moveFigure(moveFrom, moveTo, returnBack = True):

                                    return False

                            except:
                                pass


            return True


    def canMove(self, field, moveFrom, moveTo):

        directions = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

        for direction in directions:
            try:
                destination = field.getCell(moveFrom.getRow() + direction[0], moveFrom.getColumn() + direction[1])

                if destination is moveTo:
                    if destination.isEmpty():
                        return True
                    elif (destination.getPiece().getTeam() != self._team):
                        return True

            except:
                pass

        return False