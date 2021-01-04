"""
    Author: Abhishek Roushan abhishek.roushan12@gmail.com
    Description:
        Assumption: This file is only accessible to the codemaker!
        The following file contains the implementation for placing
        the pegs on board.
        Rules:
        1. A black peg (b) on a hole means both the color and positon match for the codebreaker 
        1. A white peg (w) on a hole means only the color not the positon match for the codebreaker 
        1. An empty peg (_) on a hole means neither the color nor the positon match for the codebreaker 
"""

from board import Board, BoardWrapper
from colors import Colors

class Pegs(object):
    def __init__(self, target):
        # all the pegs are empty
        self.p1 = "_"
        self.p2 = "_"
        self.p3 = "_"
        self.p4 = "_"
        self.target = target    #target board

    def decipher(self, bPlayed):
        # bPlayed = Board played
        bw = BoardWrapper(self.target)
        pegsFromBoard = bw.pegStatus(bPlayed)
        self.setPegsFromBoard(pegsFromBoard)

    def setPegsFromBoard(self, pegsFromBoard):
        self.p1 = pegsFromBoard.p1
        self.p2 = pegsFromBoard.p2
        self.p3 = pegsFromBoard.p3
        self.p4 = pegsFromBoard.p4

    def showPeg(self, p, color):
        # p=="b": show black peg
        # p=="w": show white peg
        # p=="_": show empty peg
        if p=="b":
            print(color.bg.white, color.fg.lightgrey, "o", end='')
        if p=="w":
            print(color.bg.white, color.fg.darkgrey, "o", end='')
        if p=="_":
            print(color.bg.white, color.fg.lightcyan, "x", end='')

    def displayPegs(self):
        print("pegs..")
        self.showPeg(self.p1, Colors)
        self.showPeg(self.p2, Colors)
        self.showPeg(self.p3, Colors)
        self.showPeg(self.p4, Colors)
        print(Colors.reset)
        # print(self.p1, ",", self.p2, ",", self.p3, ",", self.p4)

