import pygame
import random
from music import Music

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

    field = pygame.image.load(images[0])

    Music.playNextMusic()

    exit = False
    while not exit:
        clock.tick(FPS)

        screen.fill((0, 0, 255))
        screen.blit(field, (50, -100))

        for event in pygame.event.get():

            # Проверка закрытия окна.
            if event.type == pygame.QUIT:
                exit = True

            elif event.type == MUSIC_END:
                Music.playNextMusic()

        pygame.display.flip()

main()