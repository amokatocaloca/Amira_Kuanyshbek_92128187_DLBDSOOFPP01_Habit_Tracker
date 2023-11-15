
import pygame
from configuration import *
from habit import *
# from textbox import *
import json
pygame.init()



class Journal(pygame.sprite.Sprite):
   def __init__(self, room, x, y, habit_manager):
      self.room=room
      self.sprite_layer = journal_layer
      self.groups = self.room.all_sprites
      pygame.sprite.Sprite.__init__(self, self.groups)
      self.habit_manager = habit_manager
      self.x = x*tile_size
      self.y = y*tile_size 
      self.width = tile_size
      self.height = tile_size
      self.x_change = 0
      self.y_change = 0
      self.image = self.room.interior_spritesheet.get_image(363,1854, self.width, self.height)
      self.rect = self.image.get_rect()
      self.rect.x = self.x
      self.rect.y = self.y
      
   def interact(self, player):
        habit_manager = player.habit_manager  # You get habit_manager from the passed player instance
        messages = print("Interacting with Journal")
        while True:
            print("Choose action:")
            print("1. Create new habit")
            print("2. Delete habit")
            print("3. Display habits grouped by type")
            print("4. Display habits grouped by periodicity")
            print("5. Show habit streaks")
            print("6. Exit")
            action = input("Enter action number: ")

            if action == '1':
                self.create_habit()
                self.habit_manager.save_habits()  # Save habits to JSON after creating
            elif action == '2':
                self.delete_habit()
                self.habit_manager.save_habits()  # Save habits to JSON after deleting
            elif action == '3':
                self.display_habits_grouped_by_type()
            elif action == '4':
                self.display_habits_grouped_by_periodicity()
            elif action == '5':
                self.show_habit_streaks()
            elif action == '6':
                break  # Exit the interaction loop
            else:
                print("Invalid input. Please enter a valid action number.")

   def create_habit(self):
        habit_name = input("Enter habit name: ")  
        existing_habits = self.habit_manager.get_habits()
        for habit in existing_habits:
            if habit.name == habit_name:
                print(f"A habit with the name {habit_name} already exists.")
                return  # If a habit with the same name exists, exit the method
        # Prompt user to select habit type
        print("Choose habit type:")
        types = ["nutrition", "physical health", "hobbies"]
        for idx, t in enumerate(types, 1):
            print(f"{idx}. {t}")
        while True:
            type_choice = input("Enter the number for habit type: ")
            if type_choice in ["1", "2", "3"]:
                habit_type = types[int(type_choice) - 1]
                break
            else:
                print("Invalid input. Please choose a valid habit type.")
        
        # Ask for habit periodicity
        print("Choose habit periodicity:")
        periods = ["daily", "weekly", "monthly"]
        for idx, p in enumerate(periods, 1):
            print(f"{idx}. {p}")
        while True:
            period_choice = input("Enter the number for habit periodicity: ")
            if period_choice in ["1", "2", "3"]:
                periodicity = periods[int(period_choice) - 1]  # Set the variable 'periodicity' here
                break
            else:
                print("Invalid input. Please choose a valid habit periodicity.")
        # Validate that the input is a positive integer for habit_goal
        while True:
            habit_goal = input(f"Enter the number of {periodicity}(s) for the habit ({habit_type}): ")
            if habit_goal.isdigit() and int(habit_goal) > 0:
                habit_goal = int(habit_goal)
                break
            else:
                print("Invalid input. Please enter a positive integer.")

        # Now pass the information to HabitManager, let it handle duration calculation
        self.habit_manager.create_habit(habit_name, habit_goal, habit_type, periodicity)
        print(f"Habit of type {habit_type} with {periodicity} duration created.")
        self.habit_manager.save_habits()  # Save habits to JSON



   def delete_habit(self):
        habit_name = input("Enter the name of the habit you want to delete: ")
        self.habit_manager.delete_habit(habit_name)
        print(f"Habit {habit_name} deleted.")

   def display_habits_grouped_by_type(self):
    habits_by_type = {}
    for habit in self.habit_manager.get_habits():
        if habit.type_ not in habits_by_type:
            habits_by_type[habit.type_] = []
        habits_by_type[habit.type_].append(habit)
    
    for habit_type, habits in habits_by_type.items():
        print(f"Type: {habit_type}")
        for habit in habits:
            print(f"{habit.name} - Goal: {habit.goal}, Progress: {habit.progress}")
        print("---")

   def display_habits_grouped_by_periodicity(self):
      
        daily_habits = [habit for habit in self.habit_manager.get_habits() if habit.duration <= 7]
        weekly_habits = [habit for habit in self.habit_manager.get_habits() if 7 < habit.duration <= 30]
        monthly_habits = [habit for habit in self.habit_manager.get_habits() if habit.duration > 30]

        print("Daily Habits:")
        for habit in daily_habits:
            print(f"{habit.name} - Progress: {habit.progress}")
        print("---")
        
        print("Weekly Habits:")
        for habit in weekly_habits:
            print(f"{habit.name} - Progress: {habit.progress}")
        print("---")
        
        print("Monthly Habits:")
        for habit in monthly_habits:
            print(f"{habit.name} - Progress: {habit.progress}")
        print("---")

   def show_habit_streaks(self):
    for habit in self.habit_manager.get_habits():
        print(f"{habit.name} - Current Streak: {habit.streak} days")
