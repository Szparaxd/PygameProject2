import pygame

from textures import TextureLoader

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, group, screen,name):
        super().__init__(group)

        self.image = TextureLoader.Load_Item_Texture()
        self.position = pos
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen

        self.name = name

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def pickup():
        print('ZBIERAM!')

    def __str__(self) -> str:
        return self.name
