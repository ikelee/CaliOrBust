import math
import random
import time
import sys
from termcolor import colored, cprint

class GameBoard:
    def __init__ (self,size,density):
        self.size = size
        self.wall = 'X'
        self.density = density
        self.board = [["" for i in range(size)] for j in range(size)]
        print("gameboard created")
        self.fps = 0.1
        self.obstacle_list = []
        #print(self.board)
        for i in range(size):
            for j in range(size):
                self.board[i][j] = " "
        
    def clear_board(self):
        
        pass

    def make_obstacles(self):
        
        for i in range(self.size):
            for j in range(self.size):
                if(not(random.randint(0,self.density))):
                    self.obstacle_list.append((i,j))
                    self.board[i][j] = self.wall
        print(self.obstacle_list)
    
    def update(self):
        for i in range(self.size):
            for j in range(self.size):
                temp_text = "|" 
                temp_text = colored(temp_text, 'red')
                print(temp_text, end = '')
                cprint(str(self.board[i][j]), 'grey', end = '')
            print(colored(('|'), 'red'))
        print ("")

gameboard = GameBoard(20, 4)
gameboard.make_obstacles()
gameboard.update()