# habit.py
import pygame
import datetime
import json

class Habit:
    def __init__(self, name, goal, duration, type_, periodicity, start_date):
        self.name = name
        self.goal = goal
        self.duration = duration
        self.type_ = type_
        self.periodicity = periodicity
        self.start_date = start_date
        
        # Add initialization for the below attributes
        self.progress = 0  # Assuming initial progress is 0
        self.streak = 0  # Assuming initial streak is 0
        self.last_update_date = start_date  # or whatever logic you'd like
        self.end_date = start_date + datetime.timedelta(days=duration)  # if the duration is meant to be in days


    def update_progress(self, value):
        today = datetime.date.today()
        self.progress += value
        
        if self.progress > self.goal: 
            self.progress = self.goal
        
        self.last_update_date = today 

    def is_completed(self):
        return self.progress >= self.goal

    def is_expired(self):
        return datetime.date.today() > self.end_date
    
    def to_dict(self):
        return {
            'name': self.name,
            'goal': self.goal,
            'duration': self.duration,
            'type_': self.type_,
            'periodicity': self.periodicity,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'progress': self.progress,
            'streak': self.streak,
            'last_update_date': self.last_update_date.isoformat() if self.last_update_date else None
        }

    @classmethod
    def from_dict(cls, data):
        habit = cls(
            name=data['name'],
            goal=data['goal'],
            type_=data['type_'],
            periodicity=data['periodicity'],
            duration=data['duration'],
            start_date=datetime.date.fromisoformat(data['start_date'])
        )
        
        habit.progress = data['progress']
        habit.streak = data['streak']
        habit.end_date = datetime.date.fromisoformat(data['end_date'])
        habit.last_update_date = datetime.date.fromisoformat(data['last_update_date']) if data['last_update_date'] else None

        return habit




class HabitManager:
    def __init__(self):
        self.habits = []
        self.load_habits()
        self.books = []  # Add this line to keep track of books


    def create_habit(self, name, goal, type_, periodicity):
        duration_in_days = goal 
        if periodicity == 'weekly':
            duration_in_days *= 7 
        elif periodicity == 'monthly':
            duration_in_days *= 30 
        
        start_date = datetime.date.today()
        new_habit = Habit(name, goal, duration_in_days, type_, periodicity, start_date)
        self.habits.append(new_habit)
        self.save_habits()



    def get_habits(self):
        # If habits are not loaded, load them from JSON
        if not self.habits:
            with open('habits.json', 'r') as file:
                data = json.load(file)
                self.habits = [Habit.from_dict(habit_data) for habit_data in data]
        return self.habits

    def update_habit(self, habit_name, progress):
        today = datetime.date.today()

        for habit in self.habits:
            if habit.name == habit_name:
                # Using method to update progress and last update date.
                habit.update_progress(progress)

                # Check if the habit is expired
                if habit.is_expired():
                    print(f"Habit {habit.name} has expired!")
                    # handle expired habit

                # Check if the habit's goal is completed
                elif habit.is_completed():
                    print(f"Congratulations! You have completed the habit: {habit.name} for today!")
                    # handle completed habit

                    # Use the existing method to save and remove the completed habit
                    self.save_and_remove_completed_habits([habit])


    def update_habits_streaks(self, player):
        today = datetime.date.today()

        for habit in self.habits:
            # Check for streak based on periodicity
            if habit.periodicity == 'daily':
                self.update_daily_streak(habit, today)

            elif habit.periodicity == 'weekly':
                self.update_weekly_streak(habit, today)

            elif habit.periodicity == 'monthly':
                self.update_monthly_streak(habit, today)

    def update_daily_streak(self, habit, today):
        if habit.last_update_date == today - datetime.timedelta(days=1):
            habit.streak += 1  # increase the streak if habit is updated daily
        else:
            habit.streak = 0  # reset the streak if not updated daily

    def update_weekly_streak(self, habit, today):
        # Calculate the week number for today and last_update_date
        current_week = today.isocalendar()[1]
        last_update_week = habit.last_update_date.isocalendar()[1]

        if current_week == last_update_week:
            habit.streak += 1  # increase the streak if habit is updated weekly
        else:
            habit.streak = 0  # reset the streak if not updated weekly

    def update_monthly_streak(self, habit, today):
        # Calculate the month and year for today and last_update_date
        current_month = today.month
        last_update_month = habit.last_update_date.month
        current_year = today.year
        last_update_year = habit.last_update_date.year

        if current_month == last_update_month and current_year == last_update_year:
            habit.streak += 1  # increase the streak if habit is updated monthly
        else:
            habit.streak = 0  # reset the streak if not updated monthly


    def save_habits(self):
        habits_data = [habit.to_dict() for habit in self.habits]
        with open('habits.json', 'w') as file:
            json.dump(habits_data, file)


    def delete_habit(self, habit_name):
        habit_to_remove = next((habit for habit in self.habits if habit.name == habit_name), None)
        if habit_to_remove:
            self.habits.remove(habit_to_remove)
            # Optionally, you may want to save the habits after deleting:
            # self.save_habits()

    def get_completed_habits(self):
        try:
            with open('completed_habits.json', 'r') as file:
                habits_data = json.load(file)
                return [Habit.from_dict(habit_data) for habit_data in habits_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_and_remove_completed_habits(self, completed_habits):
        # Load current completed habits
        current_completed_habits = self.get_completed_habits()
        # completed_habits = []
        # Filter out habits that are completed
        new_completed_habits = [habit for habit in self.habits if habit.is_completed()]

        # Add the new completed habits to the list
        all_completed_habits = current_completed_habits + new_completed_habits

        # Save all completed habits to the "completed_habits.json" file
        with open('completed_habits.json', 'w') as file:
            json.dump([habit.to_dict() for habit in all_completed_habits], file)

        # Use the remove function to remove completed habits from the active habits list
        self.habits = [habit for habit in self.habits if not habit.is_completed()]

        # Save the current state of active habits to the "habits.json" file
        self.save_habits()  # Make sure to save changes to "habits.json"



    def load_habits(self):
        try:
            with open('habits.json', 'r') as file:
                try:
                    habits_data = json.load(file)
                    for habit_data in habits_data:
                        self.habits.append(Habit.from_dict(habit_data))
                except json.JSONDecodeError:
                    print("Warning: habits.json is empty or not valid JSON.")
        except FileNotFoundError:
            print("habits.json not found.")
