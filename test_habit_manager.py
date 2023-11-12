import pytest
from configuration import *
from habit import *
from journal import *
from bulletin import * 
from bookshelf import *
from player import *
from sprites import *
import os
import datetime


# Load habits from the JSON file
def load_habits_data():
    with open('//Users/amira/Desktop/final/test_habits.json', 'r') as file:
        data = json.load(file)
        return [Habit.from_dict(habit_data) for habit_data in data]

@pytest.fixture
def habit_manager():
    manager = HabitManager()
    manager.habits = load_habits_data()
    return manager

def test_update_daily_streak(habit_manager):
    daily_habit = next(habit for habit in habit_manager.habits if habit.periodicity == 'daily')
    daily_habit.update_progress(1)  # Simulate updating the habit
    habit_manager.update_habits_streaks(None)
    assert daily_habit.streak == 1

def test_update_weekly_streak(habit_manager):
    # Get the habit 'Tomato'
    weekly_habit = next(habit for habit in habit_manager.habits if habit.name == 'Tomato')
    weekly_habit.last_update_date = datetime.date(2023, 11, 8)  # last update
    habit_manager.update_habits_streaks(None)
    assert weekly_habit.streak == 4  # Expected streak

def test_update_monthly_streak(habit_manager):
    # Get the habit 'Yoga' (monthly)
    monthly_habit = next(habit for habit in habit_manager.habits if habit.name == 'Yoga' and habit.periodicity == 'monthly')
    # Ensure the last update was in the previous month
    last_month = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    monthly_habit.last_update_date = last_month
    habit_manager.update_habits_streaks(None)
    assert monthly_habit.streak == 0  # Expected streak
