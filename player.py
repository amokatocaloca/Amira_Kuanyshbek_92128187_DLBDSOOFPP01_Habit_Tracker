import pygame
from configuration import *
from sprites import *
from habit import *

class Player(pygame.sprite.Sprite):
   def __init__(self, room, x, y):
      self.room=room
      self.sprite_layer = player_layer
      self.groups = self.room.all_sprites
      pygame.sprite.Sprite.__init__(self, self.groups)

      self.x = x*tile_size
      self.y = y*tile_size
      self.width = tile_size
      self.height = tile_size
      self.x_change = 0
      self.y_change = 0
      self.image = self.room.player_spritesheet.get_image(0,0, self.width, self.height)
      self.rect = self.image.get_rect()
      self.rect.x = self.x
      self.rect.y = self.y
      self.direction = "right"
      self.habit_manager = HabitManager()

   def input(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_k]:  # Suppose 'K' is the interaction key
           self.interact_with_objects_nearby()
    
   def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x_change = self.x_change - player_steps
            self.direction = "left"
        elif key[pygame.K_d]:
            self.x_change = self.x_change + player_steps
            self.direction = "right"
        elif key[pygame.K_w]:
            self.y_change = self.y_change - player_steps
            self.direction = "up"
        elif key[pygame.K_s]:
            self.y_change = self.y_change + player_steps
            self.direction = "down"

   def want_to_interact(self):
       user_input = input("Do you want to interact with the object? (yes/no): ")
       return user_input.lower() == "yes"

   def interact_with_objects_nearby(self):
    interactables = [obj for obj in self.room.interactive_objects if self.rect.colliderect(obj.rect) and obj != self]
    if not interactables:
        print("No interactable objects nearby.")
        return
    
    for obj in interactables:
        if hasattr(obj, 'interact'):  # Check if object has interact method
            if self.want_to_interact():  # Ask the player if they want to interact
                obj.interact(self)  # Pass the player instance
            else:
                print("You chose not to interact with the object.")

   def update(self):
       self.move()
       self.rect.x = self.rect.x + self.x_change
       self.rect.y = self.rect.y + self.y_change     
       self.x_change = 0 
       self.y_change = 0 
       self.input()