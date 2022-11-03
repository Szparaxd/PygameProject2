import pygame

from textures import TextureLoader
from Bullets import Bullets


red = (255,0,0)
green = (0,255,0)
class Player2(pygame.sprite.Sprite):
    def __init__(self, pos, group,screen):
        super().__init__(group)
        self.image = TextureLoader.Load_Player_Texture()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.playerDirection = 1
        self.position = pos
        self.screen = screen

        # spawn
        self.speed = 16
        self.speedBullet = 32
        self.shootCooldown = 0
        self.alive = True
        self.health = 100
        self.healthMax = 100
        self.healthMin = self.health
        #self.lastShot = pygame.time.get_ticks()
        #self.bulletGroup = pygame.sprite.Group()
        self.shooting = False

        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        
    def draw(self):
        self.screen.blit(self.image, self.rect)\
    
    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey

    def control(self,x,y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def __str__(self) -> str:
        return 'Player'
