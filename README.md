# Habit Tracker

Welcome to the Habit Tracker, a Python-based application that transforms the routine of habit tracking into an engaging, game-like experience. Drawing inspiration from tranquil, routine-focused games like Stardew Valley, this application combines the principles of object-oriented programming with the charm of pixel art aesthetics.

## Core Features

-  Pixel Art Visuals : Thanks to LimeZu's free pixel art package (https://limezu.itch.io/moderninteriors?download), the game boasts a visually rich environment.
-  Leveraging Pygame : Utilizing Pygame's comprehensive modules, we've crafted an interactive 2D game world, featuring a detailed map, interactive objects, player movement, and responsive event mechanics.
-  Detailed Analytics : Track, analyze, and gain insights on your habits. My application monitors streaks, categorizes habits by type and frequency, and maintains historical data for trend analysis.

## User Interaction and Game Mechanics

-  Graphical Interface : The current interface is console-based due to time constraints. Text-based inputs and outputs have to be viewes through the console, however the game map is functional, focusing on key gameplay elements like navigation and object interaction. 


## Unit Tests
- First, pytest has to be installed on the computer to run tests 
``` pip install pytest ```
- The commands to run the tests are:
``` pytest test_hait.py ```
``` pytest test_habit_manager.py ```



## Habit Creation and Management Pipeline

-  Initiating the Application : Download all application files, including the assets, and run `main.py` to start the game the player in the lower right corner of the map. Use WASD keys for navigation.
- You should have Pygame installed on your computer, just use this command:

``` pip install pygame ```

-  Creating a Habit :
  1. Approach the  Journal Table  and press "K" to trigger an interaction prompt. Return to the python console and type in "yes" for the habit creation and management menu to open. 
  2. Follow prompts in the CLI to choose the option from the menu, (f.e. type in 1 to choose the first option "1. Create habit"). You can manually enter the habit's name, choose its type (e.g., exercise, reading), select periodicity (daily, weekly, monthly), and set a completion goal. The goal will be the number of dailys, monthlys, or weeklys that you need to completed for the habit depending on the periodicity chosen. 
  3. Confirm the creation and exit through the provided "Exit" option in the CLI.
-  Updating Habit Progress :
  1. Move to the  Bulletin Board  and follow the same interaction logic as with the Journal object. To enter updates on your habit's progress (e.g., number of days exercised), choose the corresponding option from the menu list "Update habit".
  2. Use the "Calculate habit streaks" function to update and track your progress streaks, to achieve a streak, you have to consistently update a habit based on the periodicity you have set. If the habit is't updated consistently, the streak ill reset to 0. 
  3. Habit completion message is announced in the console after updating the final progress in the Bulletin Board, and the habit is then archived for historical tracking. If the habit is expired, then it will be deleted permamently, with a warning message appearing in the console.
-  Viewing and Analyzing Habit Data :
  1. Return to the  Journal Table  to view a comprehensive breakdown of your habits, including grouping by type and periodicity, and viewing current streaks.
  2. Completed habits are automatically transferred to the `completed_habits.json` file for archival purposes.
  3. Using the Bookshelf object, the player can view historical data, consolidated into books of 3. Book in this case is a collection of dictionaries for 3 completed habits, their names, start and end dates, types etc. You can view the number of book and read them by using the similar menu option mechanic as for the Journal and Bulletin Board mechanic. Books are numbered, and to choose a book the player should input a corresponding number when the "Read a book" option is chosen. It will show all completed, not expired habits from all months.


## Object Functionalities and Interactions

- Journal Table : The analytics module for habit management. Interact here for habit creation, deletion, and analytics.
-  Bulletin Board : A key interface for updating and tracking habit progress, influencing streak calculations and habit completion status.
-  Bookshelf : An inventive method to archive completed habits, organizing them into 'books' for easy reference and historical overview.

## Data Synchronization and Storage

-  Real-time Syncing : Changes in habit data are instantly synchronized across the Journal, Bulletin Board, and Bookshelf, maintaining consistency and accuracy.
-  JSON Format : Habit data, including attributes like name, type, goal, periodicity, progress, and streaks, are stored in a JSON file, ensuring easy access and manageability.

## Dive into Habit Tracker

Embark on a delightful journey with Habit Tracker. While currently simple, it lays the groundwork for a more feature-rich and immersive habit-tracking experience. 

Explore, track, and enjoy the process of building healthy habits with Habit Tracker, your digital companion in personal growth and consistency! 🌟