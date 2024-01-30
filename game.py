import pygame
import sys

from scripts.utilities import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.clouds import Cloud, Clouds

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
            'decor'  : load_images('tiles/decor'),
            'grass'  : load_images('tiles/grass'),
            'large_decor'  : load_images('tiles/large_decor'),
            'stone'  : load_images('tiles/stone'),
            'player' : load_image('entities/player.png'),
            'background' : load_image('background.png'),
            'clouds' : load_images('clouds')
        }

        self.clouds = Clouds(self.assets['clouds'], count=16)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)
    
        self.scroll = [0,0]

    # run game function
    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centerx - self.display.get_height() / 2 - self.scroll[1]) / 30

            render_scroll = (int(self.scroll[0]), (self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            self.tilemap.render(self.display, offset=render_scroll)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=self.scroll)

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
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

                # WASD keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    #if event.key == pygame.K_w:
                    #    self.player.velocity[1] = -3
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -3         
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    #if event.key == pygame.K_w:
                    #    self.player.velocity[1] = 0
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = 0      

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()