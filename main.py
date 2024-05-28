import pygame
import random
from music import Music
from figures import *
from Field import *

def main():

    width = 1080 # Ширина игрового экрана.
    height = 800 # Высота игрового экрана.
    FPS = 30     # Частота кадров в секунду.

    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    Music.init()

    # Устанавливаем событие оуончания музыки.
    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)

    imagesFolder = 'Images'
    images = [imagesFolder + '\Field.png']

    field = Field(images[0])

    Music.playNextMusic()

    # Откуда и куда будет двигаться фигура.
    moveFrom = None
    moveTo = None

    # В начале ходят белые.
    isWhiteMove = True
    isBlackMove = False

    exit = False
    while not exit:
        clock.tick(FPS)

        screen.fill((0, 0, 255))
        screen.blit(field.getImage(), (100, 0))

        field.blitAllPieces(screen)

        for event in pygame.event.get():


            # Если пользователь клинкул мышкой.
            if event.type == pygame.MOUSEBUTTONUP:

                try:
                    mouceCoordinates = pygame.mouse.get_pos()
                    if pygame.mouse.get_pos() is not None:
                        cell = field.findCell(mouceCoordinates)

                        if moveFrom is None:

                            try:
                                # Могут ходить только те фигуры, чей сейчас ход!
                                if isWhiteMove and cell.getPiece().getTeam() == "white":
                                    moveFrom = (cell.getRow(), cell.getColumn())
                                elif isBlackMove and cell.getPiece().getTeam() == "black":
                                    moveFrom = (cell.getRow(), cell.getColumn())

                            except CellDontContainsPiece:
                                pass

                        else:

                            # Нельзя есть своих!
                            try:

                                if isWhiteMove and cell.getPiece().getTeam() != "white":
                                    moveTo = (cell.getRow(), cell.getColumn())
                                elif isBlackMove and cell.getPiece().getTeam() != "black":
                                    moveTo = (cell.getRow(), cell.getColumn())

                            # Если клетка не содержит фигуру.
                            except CellDontContainsPiece:
                                moveTo = (cell.getRow(), cell.getColumn())

                        if moveFrom is not None and moveTo is not None:
                            if field.moveFigure(moveFrom, moveTo):

                                # Передаем ход следующей команде.
                                isWhiteMove = not isWhiteMove
                                isBlackMove = not isBlackMove
                                moveFrom = None
                                moveTo = None

                            else:

                                # Если переместить фигуру не удалось, то заставляем игрока ходить по-другому.
                                moveFrom = None
                                moveTo = None

                except CannotFindThisCell:
                    pass


            # Проверка закрытия окна.
            elif event.type == pygame.QUIT:
                exit = True

            # Если музыка закончилась, то включаем следующую.
            elif event.type == MUSIC_END:
                Music.playNextMusic()

        pygame.display.flip()

main()