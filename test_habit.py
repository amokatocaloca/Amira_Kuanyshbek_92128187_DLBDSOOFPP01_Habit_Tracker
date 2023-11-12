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


import pytest
from habit import Habit, HabitManager
import datetime
import json

# Path to the actual JSON file
JSON_PATH = '/Users/amira/Desktop/final/test_habits.json'

# Fixture to load habits data from the actual JSON file
@pytest.fixture
def load_habits_data():
    with open(JSON_PATH, 'r') as file:
        data = json.load(file)
        return [Habit.from_dict(habit_data) for habit_data in data]

# Habit manager fixture
@pytest.fixture
def habit_manager(load_habits_data):
    manager = HabitManager()
    manager.habits = load_habits_data
    return manager

# Example test using the fixture
def test_create_habit(load_habits_data):
    for habit in load_habits_data:
        assert isinstance(habit, Habit)
        assert isinstance(habit.name, str)
        assert isinstance(habit.goal, int)

# Test update progress
def test_update_progress(load_habits_data):
    habit = load_habits_data[0]
    initial_progress = habit.progress  # Capture the current progress from the loaded data
    update_amount = 5
    habit.update_progress(update_amount)

    # If the progress exceeds the goal, it should be set to the goal value
    expected_progress = min(initial_progress + update_amount, habit.goal)
    assert habit.progress == expected_progress

# Test is_completed
def test_is_completed(load_habits_data):
    habit = load_habits_data[0]
    habit.update_progress(habit.goal)
    assert habit.is_completed() is True

# Test is_expired
def test_is_expired(load_habits_data):
    habit = load_habits_data[0]
    past_date = datetime.date.today() - datetime.timedelta(days=habit.duration + 1)
    habit.start_date = past_date
    habit.end_date = past_date + datetime.timedelta(days=habit.duration)
    assert habit.is_expired() is True
