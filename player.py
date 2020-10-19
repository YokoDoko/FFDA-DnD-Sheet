import math
import random

class Player():

    def __init__(self):
        self.level = 1
        self.name = ""
        self.classes = list()
        self.gil = 0
        self.race = ""
        self.sex = ""

    def setName(self):
        self.name = input("What is your name: ")