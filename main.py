import math
import random
import tkinter
import player
import warrior
import dice


player1 = player.Player()
player1.classes.append(warrior.Warrior())

player1.level = 10
player1.classes[0].updateStats(player1.level)
print("STA modifier:", player1.classes[0].STA)
print("Vitality:", player1.classes[0].VIT)
print("TotB Vitality:",player1.classes[0].tVIT)
print("Health:", player1.classes[0].HP)
print("TotB Health:", player1.classes[0].tHP)
print("Strength:",player1.classes[0].STR)


# top = tkinter.Tk()
# top.mainloop()