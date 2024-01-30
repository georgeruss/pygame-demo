import pygame
import sys

class Game:
    # initialize game function
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pygame platformer demo - George Landyn Russell')
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')

    # run game function
    def run(self):
        while True:
            self.screen.blit(self.img, (100, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)

