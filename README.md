# FFDA-DnD-Sheet
The goal of the project is to have a fully customizable character sheet that also includes a way to roll actions.

Please note, this is my first ever project using Python. This is purely a learning experience while also having a fundamental use in my personal life. If you for some reason find anything within my code useful for your own, feel free to use it!



I am using the "math" and "random" libraries for this project. The "math" library is mostly needed for rounding values up or down using the ceil() and floor() functions. The "random" library is essential for dice rolls thanks to the randint() function. Other functions are self-made.



Current Progress :

---> updateStats() function inside the Warrior class properly calculates stats.

---> Created "statchecker.py" to reduce repetitive if statements to calculate stats, health, and modifiers.

---> Moved the rollDice() function into a separate file called "dice.py".


# This list will be only for what I believe I should work on next. This does not represent the entirety of the project.
To-Do List :

---> Move rollDice into a file outside of "main.py" for accessibility. Other classes will need it for functions within them.

---> Find a way to move updateStats() outside of the Warrior class for reusability. Potentially 

---> Create functions for the skills of Warrior

Completed Features :

---> Stat updater
