Welcome and thank you for using my Habit Tracker application! This application is a part of our Object-Oriented Programming with Python coursework portfolio. 
My goal was to create a backend for a habit tracker using Python modules and packages. 
However, we decided to take it a step further and design this application as a game, similar to relaxing routine-based games like Stardew Valley.

## Features

- Pixel Art: The gorgeous pixel art for sprites is done by LimeZu from their free package on itch.io (https://limezu.itch.io/moderninteriors?download), adding an aesthetic touch to the game.
- Pygame Library: We've utilized the extensive selection of modules and tools provided by the Pygame library to create a proper game environment. 
This includes setting up the 2D grid game map, object layers, player movement, and event triggers.
- Analytics module: The app stores real-time data and performs analytics to display breakdown of habit streaks, habit types and historical data. 

## Important Note

- Limited GUI: Due to time constraints, I couldn't fully develop the graphical user interface (GUI) for this application. As a result, interactions such as text inputs and result outputs will be handled through the console. 
The game map lacks borders, and the collision system is minimal. The primary game mechanics include the game map, player movement, and interaction with objects.

## Getting Started

To initialize the application, simply run the `main.py` file. This will create the game map and all the necessary functionalities. 
The player initially appears on the lower right corner of the map and can move freely using the WASD keys.

## Interacting with Objects

Three objects are present on the map: a table with a journal, a floating bulletin board, and a bookshelf. 
To interact with an object, approach it closely and press the "K" key on the keyboard. An interaction prompt will appear in the console, and the player will need to provide a manual yes/no answer.

If "yes" is chosen, a numbered list of options will be displayed in the console. To trigger an action, enter the corresponding number in the console. 
Upon completion, a confirmation message will appear, along with results if the action requires text output.

## Object Functionalities and Analytics

- The Journal acts as the key analytics module, containted within the journal.py file. It calls the majority of the Habit class and Habit Manager class habits 
to processand breakdown the habit tracking activity in insightful forms. It offers 5 options for analytics:
1. Create habit.
2. Delete Habit.
3. Display habits grouped by type.
4. Display habits grouped by periodicity.
5. Show habit streaks.
The outcome of these options and the changes made to habit data through them are synched with the Bulletin Board and the Booksheld objects.

- The Bulletin Board mainly works as an input and input processing object, the end result of which can be seen by interacting with the Journal (show streaks),
and the Bookshelf (stores and organizes historical data). You can update habits by entering the number of dailys, monthlys, and weeklys you have completed
for a certain habit, and click to calculate habit streaks, which then can be seen in the Journal. 

- The Bookshelf organizes completed habits into books of three habits. Each book is a dictionary storing the habit data along with their start and end date, streaks, periodicity and last update date.

## Data Synchronization

Objects have a two-way synchronization with each other. When new data is created or updated, it is saved in a JSON file representing the stages of completion for each habit, structured like a dictionary.
A habit includes attributes such as name, type, goal, periodicity, start date, end date, progress, streaks, and last update date.