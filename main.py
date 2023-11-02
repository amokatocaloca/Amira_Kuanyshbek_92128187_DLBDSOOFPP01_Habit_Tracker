import json
import datetime
import sys 

from configuration import *
from sprites import *
from player import *
from habit import Habit, HabitManager
from journal import *
from bulletin import *
from bookshelf import * 

# In your main.py or equivalent


pygame.init()


class Spritesheet:
   def __init__(self, path):
      self.spritesheet = pygame.image.load(path).convert()

   def get_image(self, x, y, width, height):
      sprite = pygame.Surface([width, height])
      sprite.blit(self.spritesheet, (0,0), (x, y, width,height))
      sprite.set_colorkey(BLACK)

      return sprite



class Room: 
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.room_spritesheet = Spritesheet('assets/Interiors/48x48/room.png')
        self.interior_spritesheet = Spritesheet('assets/Interiors/48x48/interior.png')
        self.player_spritesheet = Spritesheet('assets/Interiors/48x48/merchant.png')
        self.running = True
        self.habit_manager = HabitManager()
        self.interactive_objects = []  # You'll need to populate this with your interactive objects
        # Inside __init__ method of Room class
        self.interacting_with_journal = False

        
    def createRoomMap(self):
       for i, row in enumerate(room_map):
          for j, column in enumerate(row):
             Ground(self, j, i)
             if column == 'B':
                Block(self, j, i)
             elif column == 'P':
               self.player = Player(self, j, i)  # Set self.player to the Player instance
               self.interactive_objects.append(self.player)  # Also add it to interactive_objects if necessary
             elif column == 'J':
                 journal = Journal(self, j, i, self.habit_manager)
                 self.interactive_objects.append(journal)
             elif column == 'S':
                bookshelf = Bookshelf(j, i, self.habit_manager, self)
                self.interactive_objects.append(bookshelf)
             elif column == 'U':
                 bulletin = BulletinBoard(self, j, i, self.habit_manager)
                 self.interactive_objects.append(bulletin)


    def create(self):
       self.all_sprites = pygame.sprite.LayeredUpdates()
       self.blocks = pygame.sprite.LayeredUpdates()
       self.createRoomMap()

    def update(self):
        self.all_sprites.update()
                     
    def events(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
               self.running = False
         # elif event.type == pygame.KEYDOWN:  # New condition to check for key press events
         #       if event.key == pygame.K_k:  # Check if the pressed key is 'K'6

         #          self.check_interaction()  # Now call the interaction check here
       
    def check_interaction(self):
         if not self.player:
            return  # Exit if player isn't set

         for obj in self.interactive_objects:
            if obj != self.player:  # Ensure we're not interacting with the player itself
                  distance = ((self.player.rect.x - obj.rect.x)**2 + (self.player.rect.y - obj.rect.y)**2)**0.5
                  interaction_key_pressed = pygame.key.get_pressed()[pygame.K_k]
                  if distance < 50 and interaction_key_pressed:  # Increased distance threshold
                     obj.interact(self.player)

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
        # If HabitManager's draw method is implemented, you may call it here with the appropriate parameters

    def main(self):
     while self.running:
         self.events()
         self.update()
         self.draw()
game = Room()
game.create()
while game.running:
   game.main()