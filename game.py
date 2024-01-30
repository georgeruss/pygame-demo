import pygame
import sys

from scripts.utilities import load_image
from scripts.entities import PhysicsEntity

class Game:
    # initialize game function
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pygame platformer demo - George Landyn Russell')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0,0,0))

        self.img_pos = [160, 260]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)

        self.assets = {
            'player' : load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    # run game function
    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # arrow keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

                # WASD keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()