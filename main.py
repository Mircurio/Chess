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

    field = Field(imagesFolder + '\Field.png')


    Music.playNextMusic()

    exit = False
    while not exit:
        clock.tick(FPS)

        screen.fill((0, 0, 255))
        screen.blit(field.getImage(), (100, 0))

        field.blitAllPieces(screen)

        for event in pygame.event.get():

            # Проверка закрытия окна.
            if event.type == pygame.MOUSEBUTTONUP:

                try:
                    mouceCoordinates = pygame.mouse.get_pos()
                    if pygame.mouse.get_pos() is not None:
                        cell = field.findCell(mouceCoordinates)

                except CannotFindThisCell:
                    pass


            elif event.type == pygame.QUIT:
                exit = True

            # Если музыка закончилась, то включаем следующую.
            elif event.type == MUSIC_END:
                Music.playNextMusic()

        pygame.display.flip()

main()