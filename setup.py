"""
    Author: Abhishek Roushan abhishek.roushan12@gmail.com
    Description:
        Assumption: This file is only accessible for the codemaker!
        The following file contains the implementation of setting up the target for the codemaker
"""
import random
from board import Board

class Setup(object):
    def __init__(self):
        self.colors = ["r", "g", "b", "y"]

    def getTarget(self):
        # chose from self.colors randomly w replacement
        b = Board()
        x = random.choice(self.colors)
        y = random.choice(self.colors)
        z = random.choice(self.colors)
        w = random.choice(self.colors)
        b.fromChr(x,y,z,w)
        return b
        
