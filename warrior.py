import player
import random
import math

class Warrior(player.Player):
    def __init__(self):
        self.baseHP = 30
        self.HP = 30
        self.STR = 5
        self.DEX = 2
        self.VIT = 6
        self.INT = 2
        self.MND = 3
        self.STA = 0
        self.AoE = 0
        self.Blk = 0
        self.tVIT = 0
        self.tHP = 0
    
    def updateStats(self):
        if (self.HP == self.baseHP + math.ceil(self.VIT / 2)):
            return
        else:
            self.HP = self.baseHP + math.ceil(self.VIT / 2)

    