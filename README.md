# Habit Tracker

Welcome to the Habit Tracker, a Python-based application that transforms the routine of habit tracking into an engaging, game-like experience. Drawing inspiration from tranquil, routine-focused games like Stardew Valley, this application combines the principles of object-oriented programming with the charm of pixel art aesthetics.

## Core Features

- **Pixel Art Visuals**: Thanks to LimeZu's free pixel art package (https://limezu.itch.io/moderninteriors?download), the game boasts a visually rich environment.
- **Leveraging Pygame**: Utilizing Pygame's comprehensive modules, we've crafted an interactive 2D game world, featuring a detailed map, interactive objects, player movement, and responsive event mechanics.
- **Detailed Analytics**: Track, analyze, and gain insights on your habits. Our application monitors streaks, categorizes habits by type and frequency, and maintains historical data for trend analysis.

## User Interaction and Game Mechanics

- **Graphical Interface**: The current interface is console-based due to time constraints. This entails text-based inputs and outputs, with a basic map focusing on key gameplay elements like navigation and object interaction.

## Habit Creation and Management Pipeline

- **Initiating the Application**: Run `main.py` to start the game, placing the player in the lower right corner of the map. Use WASD keys for navigation.
- **Creating a Habit**:
  1. Approach the **Journal Table** and press "K" to open the habit creation interface.
  2. Follow prompts in the CLI to enter the habit's name, choose its type (e.g., exercise, reading), select periodicity (daily, weekly, monthly), and set a completion goal.
  3. Confirm the creation and exit through the provided "Exit" option in the CLI.
- **Updating Habit Progress**:
  1. Move to the **Bulletin Board** and interact to enter updates on your habit's progress (e.g., number of days exercised).
  2. Utilize the "Calculate habit streaks" function to update and track your progress streaks.
  3. Habit completion is announced here, and the habit is then archived for historical tracking.
- **Viewing and Analyzing Habit Data**:
  1. Return to the **Journal Table** to view a comprehensive breakdown of your habits, including grouping by type and periodicity, and viewing current streaks.
  2. Completed habits are automatically transferred to the `completed_habits.json` file for archival purposes.

## Object Functionalities and Interactions

- **Journal Table**: The epicenter for habit analytics and management. Interact here for habit creation, deletion, and analytics.
- **Bulletin Board**: A key interface for updating and tracking habit progress, influencing streak calculations and habit completion status.
- **Bookshelf**: An inventive method to archive completed habits, organizing them into 'books' for easy reference and historical overview.

## Data Synchronization and Storage

- **Real-time Syncing**: Changes in habit data are instantly synchronized across the Journal, Bulletin Board, and Bookshelf, maintaining consistency and accuracy.
- **JSON Format**: Habit data, including attributes like name, type, goal, periodicity, progress, and streaks, are stored in a JSON file, ensuring easy access and manageability.

## Dive into Habit Tracker

Embark on a delightful journey with Habit Tracker. While currently simple, it lays the groundwork for a more feature-rich and immersive habit-tracking experience. 

Explore, track, and enjoy the process of building healthy habits with Habit Tracker, your digital companion in personal growth and consistency! 🌟