import pygame
import sys

from scripts.utilities import load_images
from scripts.tilemap import Tilemap

RENDER_SCALE = 2.0

class Editor:
    # initialize game function
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pygame platformer demo - editor')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.assets = {
            'decor'  : load_images('tiles/decor'),
            'grass'  : load_images('tiles/grass'),
            'large_decor'  : load_images('tiles/large_decor'),
            'stone'  : load_images('tiles/stone'),
        }

        self.movement = [False, False, False, False]

        self.tilemap = Tilemap(self, tile_size=16)
    
        self.scroll = [0,0]

    # run game function
    def run(self):
        while True:
            self.display.fill((0,0,0))

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
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False

                # WASD keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True  
                    if event.key == pygame.K_s:
                        self.movement[3] = True           
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False     
                    if event.key == pygame.K_w:
                        self.movement[2] = False  
                    if event.key == pygame.K_s:
                        self.movement[3] = False  
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Editor().run()