import pygame

from configuration import *
from habit import *

class Block(pygame.sprite.Sprite):
    def __init__ (self, room, x, y):

        self.room = room 
        self.sprite_layer = blocks_layer
        self.groups = self.room.all_sprites, self.room.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*tile_size
        self.y = y*tile_size 
        
        self.width = tile_size
        self.height = tile_size
        self.image = self.room.interior_spritesheet.get_image(6,2369, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    def __init__ (self, room, x, y):
       
        self.room = room 
        self.sprite_layer = ground_layer
        self.groups = self.room.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x*tile_size
        self.y = y*tile_size 
        
        self.width = tile_size
        self.height = tile_size
        self.image = self.room.room_spritesheet.get_image(528,624, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

 