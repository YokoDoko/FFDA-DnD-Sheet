# FFDA-DnD-Sheet
The goal of the project is to have a fully customizable character sheet that also includes a way to roll actions.

# Please note, this is my first ever project using Python. This is purely a learning experience while also having a fundamental use in my personal life. If you for some reason find anything within my code useful for your own, feel free to use it!

I am using the "math" and "random" libraries for this project. The "math" library is mostly needed for rounding values up or down using the ciel() and floor() functions. The "random" library is essential for dice rolls thanks to the randint() function.

Current Progress :
---> Successfully made a Player class that can nest a list of other classes inside of it. This is so a player can be listed under multiple classes (such as Warrior, Bard, and Astrologian).
---> Successfully made a function to roll a dice. The default minimum value is 1, as a dice should not be able to roll a 0.
---> Made a function that will update the stats to be proper values using formulas I made.

# This list will be only for what I believe I should work on next. This does not represent the entirety of the project.
To-Do List :
---> Move rollDice into a file outside of "main.py" for accessibility. Other classes will need it for functions within them.
---> Finish the updateStats function within Warrior.
---> Contemplate another way of doing classes, as a lot of repetition with variables such as Health Points, Strength, Dexterity, and etc. may occur.

Completed Features :
---> Currently none.
