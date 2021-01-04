"""
    Author: Abhishek Roushan abhishek.roushan12@gmail.com
    Description:
        Assumption: This file is publicly accessible for both the codemaker and codebreaker!
        The following file contains the implementation of the game
"""

from board import Board, BoardWrapper
from pegs import Pegs
from setup import Setup
from colors import Colors

class MasterMind(object):
    def __init__(self, moves:int):
        # moves = number of moves given to the codebreaker to break the code
        # only store the last instance of move played
        self.moves = moves
        self.target = None
        self.setupTarget()
        self.board = Board()
        self.pegs = Pegs(self.target)

    def placeMove(self, b):
        # b:Board
        # this changes self.board and self.pegs
        self.board = b
        self.pegs.decipher(b)
        self.moves -=1
    def solved(self):
        return self.board.matches(self.target)

    def displayResult(self):
        self.pegs.displayPegs()

    def setupTarget(self, show=False):
        s = Setup()
        self.target = s.getTarget()
        if show:
            print("target..")
            self.target.displayBoard()

def displayInput(b:str):
    # ex input str - brgy
    # to print: colored O s with white bg and this particular color fg
    for ch in b:
        if ch=="r":
            print(Colors.bg.white, Colors.fg.red, "O", end='')
        if ch=="b":
            print(Colors.bg.white, Colors.fg.blue, "O", end='')
        if ch=="g":
            print(Colors.bg.white, Colors.fg.green, "O", end='')
        if ch=="y":
            print(Colors.bg.white, Colors.fg.yellow, "O", end='')
    print()
    print(Colors.reset)

def playMasterMind():
    numMoves = 12
    m = MasterMind(numMoves)
    solved = False
    while m.moves>0:
        print("---------------------------")
        b = input("Fill in your guess..")
        print("you filled - ")
        displayInput(b)
        bs = Board()
        bs.fromString(b)
        m.placeMove(bs)
        if m.solved(): 
            solved=True
            break
        m.displayResult()
    if solved:
        print("Congratulations, you broke the code..!")
    else:
        print("Better luck next time. The code was..")
    m.displayResult()

playMasterMind()
