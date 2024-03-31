import pygame
import random

def main():
    width = 1080 # Ширина игрового экрана.
    height = 800 # Высота игрового экрана.
    FPS = 30 # Частота кадров в секунду.

    pygame.init()
    pygame.mixer.init() # Для звука.
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    '''
    Spring Flowers by Keys of Moon | https://soundcloud.com/keysofmoon
    Music promoted by https://www.chosic.com/free-music/all/
    Creative Commons CC BY 4.0
    https://creativecommons.org/licenses/by/4.0/

    Morning Routine by Ghostrifter Official | https://soundcloud.com/ghostrifter-official
    Music promoted by https://www.chosic.com/free-music/all/
    Creative Commons CC BY-SA 3.0
    https://creativecommons.org/licenses/by-sa/3.0/

    Ithilien by Spheriá | https://soundcloud.com/spheriamusic
    Music promoted by https://www.chosic.com/free-music/all/
    Creative Commons CC BY-SA 3.0
    https://creativecommons.org/licenses/by-sa/3.0/
    '''
    musicFolder = 'Music'
    musicLibrary = [ musicFolder + '\Spring Flowers.mp3', musicFolder + '\Morning-Routine.mp3', musicFolder + '\Ithilien-chosic.mp3']

    # randomMusicNumber = random.randint(0, len(musicLibrary))
    # pygame.mixer.music.load(musicLibrary[0])
    # pygame.mixer.music.queue(musicLibrary[1])
    # pygame.mixer.music.queue(musicLibrary[2])
    #
    # pygame.mixer.music.play()

    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)

    # Создаём случайную очередь музыки.
    musicQueue = []

    imagesFolder = 'Images'
    images = [imagesFolder + '\Field.png']

    field = pygame.image.load(images[0])

    while len(musicQueue) != len(musicLibrary):
        randomMusic = random.randint(0, len(musicLibrary) - 1)

        if randomMusic not in musicQueue:
            musicQueue.append(randomMusic)

    # Текущая музыка.
    currentMusic = 0
    pygame.mixer.music.load(musicLibrary[musicQueue[currentMusic]])
    pygame.mixer.music.play()

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

                if currentMusic < len(musicQueue) - 1:
                    currentMusic += 1
                else:
                    currentMusic = 0

                pygame.mixer.music.load(musicLibrary[musicQueue[currentMusic]])
                pygame.mixer.music.play()


        pygame.display.flip()

main()