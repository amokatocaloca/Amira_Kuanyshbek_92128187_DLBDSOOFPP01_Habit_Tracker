from configuration import *
from player import * 
import pygame
from configuration import *
from habit import *
import json
import os

pygame.init()

class Bookshelf(pygame.sprite.Sprite):
    def __init__(self, x, y, habit_manager, room):
        self.room=room
        self.sprite_layer = bookshelf_layer
        self.groups = self.room.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.habit_manager = habit_manager
        self.x = x*tile_size
        self.y = y*tile_size 
        self.width = tile_size
        self.height = tile_size
        self.x_change = 0
        self.y_change = 0
        self.image = self.room.interior_spritesheet.get_image(308,890, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.books = []
        self.books_file = "books.json"
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r') as f:
                self.books = json.load(f)
        else:
            self.books = []

    def save_books(self):
        with open(self.books_file, 'w') as f:
            json.dump(self.books, f)

    def interact(self, player):
        print("Interacting with Bookshelf")
        while True:
            print("Choose action:")
            print("1. Display books on shelf")
            print("2. Read a book")
            print("3. Organize habits into books")
            print("4. Exit")
            action = input("Enter action number: ")

            if action == '1':
     
                self.display_books_on_shelf()
            elif action == '2':
                 book_number = int(input("Enter the number of the book you want to read: "))
                 self.read_book(book_number)
            elif action == '3':
                self.organize_habits_into_books()
            elif action == '4':
                break  # Exit the interaction loop
            else:
                print("Invalid input. Please enter a valid action number.")

    def organize_habits_into_books(self):
        completed_habits = self.habit_manager.get_completed_habits()

        # Filter out the new habits, i.e., habits not already in books
        new_habits = [habit for habit in completed_habits if not self.habit_exists_in_books(habit)]

        # Check if there are at least 3 new habits
        if len(new_habits) >= 3:
            # Create a new book with the new habits
            new_book = {
                'habits': [{'habit': habit.to_dict()} for habit in new_habits[:3]]
            }
            self.books.append(new_book)  # Append the new book to self.books

            # Remove these new habits from the active habits list
            self.habit_manager.save_and_remove_completed_habits(new_habits[:3])

            # Save the updated books
            self.save_books()

            print("Habits have been organized into a new book.")
        else:
            print("Not enough new habits to create a book.")

    def habit_exists_in_books(self, habit):
        for book in self.books:
            for book_habit_data in book['habits']:
                book_habit = book_habit_data['habit']
                if habit.to_dict() == book_habit:
                    return True
        return False

    def display_books_on_shelf(self):
        for index, book in enumerate(self.books, 1):
          print(f"Book {index} contains {len(book['habits'])} habits.")

        if not self.books:
                    print("The bookshelf is empty.")
                    return

    def read_book(self, book_number):
        if book_number < 1 or book_number > len(self.books):
            print("Invalid book number.")
            return

        book = self.books[book_number - 1]  # Adjust index to match list indexing
        habits = book["habits"]  # Access the list of habits within the book

        print(f"Reading Book {book_number}:")
        for idx, habit_data in enumerate(habits, start=1):
            habit = habit_data["habit"]  # Access the habit dictionary within the habit_data
            print(f"Habit {idx}:")
            print(f"Name: {habit['name']}")
            print(f"Start Date: {habit['start_date']}")
            print(f"End Date: {habit['end_date']}")
            print(f"Periodicity: {habit['periodicity']}")
            print(f"Streak: {habit['streak']}")
            print(f"Type: {habit['type_']}")

        if not habits:
            print("This book has no habits.")

        if not self.books:
            print("The bookshelf is empty.")
