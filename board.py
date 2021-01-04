"""
    Author: Abhishek Roushan abhishek.roushan12@gmail.com
    Description:
        Assumption: This file is publicly accessible for both the codemaker and codebreaker!
        The following file contains the implementation of a code on board
"""

class Board(object):
    def __init__(self):
        self.p1 = "_"
        self.p2 = "_"
        self.p3 = "_"
        self.p4 = "_"
    def fromChr(self, p1, p2, p3, p4):
        # p1-p4 are colors at position 1-4 of the board code
        # p1-p4: str
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    def matches(self, b):
        return self.p1==b.p1 and\
                self.p2==b.p2 and\
                self.p3==b.p3 and\
                self.p4==b.p4

    def fromString(self, b:str):
        self.p1 = b[0]
        self.p2 = b[1]
        self.p3 = b[2]
        self.p4 = b[3]

    def displayBoard(self):
        print(self.p1, ",", self.p2, ",", self.p3, ",", self.p4)
   
class BoardWrapper(object):
    def __init__(self, target):
        self.target = target
    def pegStatus(self, board):
        # board: Board
        # given the state of the board, and self.target
        # return status of the pegs as Board obj
        pegs = Board()
        # correct pos and correct color
        if board.p1 == self.target.p1: pegs.p1 = "b"
        if board.p2 == self.target.p2: pegs.p2 = "b"
        if board.p3 == self.target.p3: pegs.p3 = "b"
        if board.p4 == self.target.p4: pegs.p4 = "b"
        # incorrect pos and correct color
        if board.p1!=self.target.p1 and board.p1 in [self.target.p2, self.target.p3, self.target.p4]: pegs.p1 = "w"
        if board.p2!=self.target.p2 and board.p2 in [self.target.p1, self.target.p3, self.target.p4]: pegs.p2 = "w"
        if board.p3!=self.target.p3 and board.p3 in [self.target.p1, self.target.p2, self.target.p4]: pegs.p3 = "w"
        if board.p4!=self.target.p4 and board.p4 in [self.target.p1, self.target.p2, self.target.p3]: pegs.p4 = "w"
        return pegs

