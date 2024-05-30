import pygame

class ImagesLibrary:
    '''Этот библиотека содержит все изображения, кроме фигур.'''

    def __init__(self):
        self.__imagesFolder = "Images"

        self.__imagesNames = [  self.__imagesFolder + "\Field.png",
                                self.__imagesFolder + "\whiteTeamWins.png",
                                self.__imagesFolder + "\\blackTeamWins.png",
                                self.__imagesFolder + "\whiteMove.png",
                                self.__imagesFolder + "\\blackMove.png"]

        self.__field = pygame.image.load(self.__imagesNames[0]).convert_alpha()
        self.__whiteTeamWins = pygame.image.load(self.__imagesNames[1]).convert_alpha()
        self.__blackTeamWins = pygame.image.load(self.__imagesNames[2]).convert_alpha()
        self.__whiteMove = pygame.image.load(self.__imagesNames[3]).convert_alpha()
        self.__blackMove = pygame.image.load(self.__imagesNames[4]).convert_alpha()

    def blitWhiteTeamWins(self, screen, center):
        screen.blit(self.__whiteTeamWins, self.__whiteTeamWins.get_rect(center = center))

    def blitBlackTeamWins(self, screen, center):
        screen.blit(self.__whiteTeamWins, self.__whiteTeamWins.get_rect(center = center))

    def blitField(self, screen, rect):
        screen.blit(self.__field, rect)

    def blitWhiteMove(self, screen, center):
        screen.blit(self.__whiteMove, self.__whiteMove.get_rect(center = center))

    def blitBlackMove(self, screen, center):
        screen.blit(self.__blackMove, self.__blackMove.get_rect(center = center))