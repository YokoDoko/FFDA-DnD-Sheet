import math
import random
import tkinter
import player
import warrior

def rollDice(amount, max, min = 1):
    sum = 0
    for _ in range(amount):
        sum += random.randint(min, max)
    print (str(amount) + "d" + str(max), "=", str(sum))

player1 = player.Player()
player1.classes.append(warrior.Warrior())

player1.classes[0].updateStats()
print(player1.classes[0].HP)


# top = tkinter.Tk()
# top.mainloop()