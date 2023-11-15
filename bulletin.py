
import pygame
from habit import *
from configuration import *
class BulletinBoard(pygame.sprite.Sprite):
    def __init__(self, room, x, y, habit_manager):
        self.room = room
        self.sprite_layer = bulletin_layer  
        self.groups = self.room.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size 
        self.y = y * tile_size  
        self.width = tile_size  
        self.height = tile_size 
        self.image = self.room.interior_spritesheet.get_image(8, 1967, self.width, self.height)  
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        self.habit_manager = habit_manager

    def interact(self, player):
        habit_manager = player.habit_manager

        print("Interacting with Bulletin Board")
        while True:
            print("Choose action:")
            print("1. Update habit")
            print("2. Calculate Streaks")
            print("3. Exit")
            action = input("Enter action number: ")

            if action == '1':
                self.update_habit(player)
      
            elif action == '2':
                self.calculate_streaks(player)  # Add a function to calculate streaks
            elif action == '3':
                break  # Exit the interaction loop
            else:
                print("Invalid input. Please enter a valid action number.")

    def update_habit(self, player):
        # Filter habits to get those that are not completed
        habits = [habit for habit in self.habit_manager.get_habits() if not habit.is_completed()]

        if not habits:
            print("No habits available to update.")
            return

        print("Select a habit to update:") 
        for idx, habit in enumerate(habits, start=1):
            print(f"{idx}. {habit.name}")

        while True:
            try:
                habit_choice = int(input("Enter the number of the habit to update: "))
                if 1 <= habit_choice <= len(habits):
                    selected_habit = habits[habit_choice - 1]
                    break  # Exit the loop once a valid input is received
                else:
                    print(f"Please enter a number between 1 and {len(habits)}.")
            except ValueError:  # Catch non-integer inputs
                print("Invalid input. Please enter a number.")

        progress = int(input(f"Enter progress made on {selected_habit.name}: "))
        self.habit_manager.update_habit(selected_habit.name, progress)
        if selected_habit.is_expired:
          print(f"Habit {habit.name} has expired!")
          self.habit_manager.delete_habit(selected_habit.name)
        else:
         print(f"Habit {selected_habit.name} updated.")
         self.habit_manager.save_habits()

        # Check if the habit is completed after the update
        if selected_habit.is_completed():
            print(f"Congratulations! Habit {selected_habit.name} is completed!")
        else:
            remaining = selected_habit.goal - selected_habit.progress
            print(f"You have {remaining} more to go to complete the habit '{selected_habit.name}'.")

    def calculate_streaks(self, player):
        # Call the habit manager's update_habit method to calculate streaks
        self.habit_manager.update_habits_streaks(player)
        print("Streaks calculated successfully.")
