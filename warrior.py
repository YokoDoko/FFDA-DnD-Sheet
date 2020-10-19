import statchecker
import random
import math

class Warrior():
    def __init__(self):
        self.tank = True
        self.baseHP = 30
        self.HP = 30
        self.baseSTR = 5
        self.STR = 5
        self.baseDEX = 2
        self.DEX = 2
        self.baseVIT = 6
        self.VIT = 6
        self.baseINT = 2
        self.INT = 2
        self.baseMND = 3
        self.MND = 3
        self.STA = 0
        self.AoE = 0
        self.Blk = 0
        self.tVIT = 0
        self.tHP = 0
        
    def updateStats(self, level):
        # 1 Strength per level
        self.STR = statchecker.statCheck(self.STR, self.baseSTR, 1, level)

        # 1 Dexterity every 2 levels
        self.DEX = statchecker.statCheck(self.DEX, self.baseDEX, 1/2, level)
        
        # 2 Vitality per level
        self.VIT = statchecker.statCheck(self.VIT, self.baseVIT, 2, level)

        # 1 Intelligence every 3 levels
        self.INT = statchecker.statCheck(self.INT, self.baseINT, 1/3, level)

        # 1 Mind every 2 levels
        self.MND = statchecker.statCheck(self.MND, self.baseMND, 1/2, level)

        # Updates HP value with current Vitality.
        self.HP = statchecker.healthCheck(self.HP, self.baseHP, self.VIT, self.tank)
        
        # Updates Single-Target Attack modifier
        self.STA = statchecker.modCheck(self.STA, self.STR, 3)

        # Updates Area of Effect attack modifier
        self.AoE = statchecker.modCheck(self.AoE, self.STR, 6)

        # Updates Block/Evasion modifier
        self.Blk = statchecker.modCheck(self.Blk, self.DEX, 5)

        # Thrill of the Battle's vitality bonus
        self.tVIT = math.ceil(self.VIT * 1.2)

        # Thrill of the Battle's HP bonus
        self.tHP = statchecker.healthCheck(self.tHP, self.baseHP, self.tVIT, self.tank)