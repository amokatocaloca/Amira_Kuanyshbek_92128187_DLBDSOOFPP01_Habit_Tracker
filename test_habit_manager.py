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
from unittest.mock import patch
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
    with patch('datetime.date') as mock_date:
        mock_today = datetime.date(2023, 11, 15)  # Mocked date
        mock_date.today.return_value = mock_today

        daily_habit = next(habit for habit in habit_manager.habits if habit.periodicity == 'daily')
        daily_habit.last_update_date = mock_today
        daily_habit.update_progress(1)  # Simulate updating the habit
        habit_manager.update_habits_streaks(None)
        assert daily_habit.streak == 1  # Expected streak

def test_update_weekly_streak(habit_manager):
    with patch('datetime.date') as mock_date:
        # Set a date within the same week as Nov 8, 2023
        mock_today = datetime.date(2023, 11, 9)
        mock_date.today.return_value = mock_today

        weekly_habit = next(habit for habit in habit_manager.habits if habit.name == 'Tomato')
        weekly_habit.last_update_date = datetime.date(2023, 11, 8)  # Last update
        habit_manager.update_habits_streaks(None)
        assert weekly_habit.streak == 4  # Expected streak


def test_update_monthly_streak(habit_manager):
    with patch('datetime.date') as mock_date:
        # Set a date within the same month and year
        mock_today = datetime.date(2023, 11, 15)
        mock_date.today.return_value = mock_today

        monthly_habit = next(habit for habit in habit_manager.habits if habit.name == 'Yoga' and habit.periodicity == 'monthly')
        monthly_habit.last_update_date = datetime.date(2023, 10, 15)  # Last update in the same month
        habit_manager.update_habits_streaks(None)
        assert monthly_habit.streak == 2  # Expected streak


