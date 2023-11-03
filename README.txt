Welcome and thank you for using my Habit Tracker application! This application is a part of our Object-Oriented Programming with Python coursework portfolio. Our goal was to create a backend for a habit tracker using Python modules and packages. However, we decided to take it a step further and design this application as a game, similar to relaxing routine-based games like Stardew Valley.

## Features

- Pixel Art: The gorgeous pixel art for sprites is done by LimeZu from their free package on itch.io (https://limezu.itch.io/moderninteriors?download), adding an aesthetic touch to the game.
- Pygame Library: We've utilized the extensive selection of modules and tools provided by the Pygame library to create a proper game environment. This includes setting up the 2D grid game map, object layers, player movement, and event triggers.

## Important Note

- Limited GUI: Due to time constraints, I couldn't fully develop the graphical user interface (GUI) for this application. As a result, interactions such as text inputs and result outputs will be handled through the console. The game map lacks borders, and the collision system is minimal. The primary game mechanics include the game map, player movement, and interaction with objects.

## Getting Started

To initialize the application, simply run the `main.py` file. This will create the game map and all the necessary functionalities. The player initially appears on the lower right corner of the map and can move freely using the WASD keys.

## Interacting with Objects

Three objects are present on the map: a table with a journal, a floating bulletin board, and a bookshelf. To interact with an object, approach it closely and press the "K" key on the keyboard. An interaction prompt will appear in the console, and the player will need to provide a manual yes/no answer.

If "yes" is chosen, a numbered list of options will be displayed in the console. To trigger an action, enter the corresponding number in the console. Upon completion, a confirmation message will appear, along with results if the action requires text output.

## Object Functionalities

- The Journal: Create, delete, display habits grouped by type/periodicity, and show habit streaks.
- The Bulletin Board**: Update habits and calculate streaks.
- The Bookshelf: Organize completed habits into books of three habits, display the books, and read a book. Each book is a dictionary containing data for three completed habits.

## Data Synchronization

Objects have a two-way synchronization with each other. When new data is created or updated, it is saved in a JSON file representing the stages of completion for each habit, structured like a dictionary. A habit includes attributes such as name, type, goal, periodicity, start date, end date, progress, streaks, and last update date.