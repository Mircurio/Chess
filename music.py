import pygame
import random

class Music:

    __musicFolder = 'Music'
    __musicLibrary = [__musicFolder + '\Spring Flowers.mp3', __musicFolder + '\Morning-Routine.mp3', __musicFolder + '\Ithilien-chosic.mp3']

    # Очередь музыки(плейлист).
    __musicQueue = []

    #Текущая музыка.
    __currentMusic = 0

    @staticmethod
    def generateRandomQueue():
        while len(Music.__musicQueue) != len(Music.__musicLibrary):
            randomMusic = random.randint(0, len(Music.__musicLibrary) - 1)

            if randomMusic not in Music.__musicQueue:
                Music.__musicQueue.append(randomMusic)

    @staticmethod
    def init(randomQueue = True):
        pygame.mixer.init()  # Для звука.

        if randomQueue:
            Music.generateRandomQueue()

    @staticmethod
    def playNextMusic():

        # Определяем допустимый диапазон.
        if Music.__currentMusic < len(Music.__musicQueue) - 1:
            Music.__currentMusic = Music.__currentMusic + 1
        else:
            Music.__currentMusic = 0

        # Проигрываем музыку из очереди.
        pygame.mixer.music.load(Music.__musicLibrary[Music.__musicQueue[Music.__currentMusic]])
        pygame.mixer.music.play()