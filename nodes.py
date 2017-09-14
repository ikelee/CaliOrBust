#Sept 12, 
#Ike Lee
#Development Cycle 1 of Fall 2017 Coop project 
#Nodes: Game designed to emulate cyber attack 

class Gameboard: 
	def __init__ (self, size):
		self.size = size
		self.board = [[' ']*size for _ in range(size)]


	def update(self):
	    for x in range(len(self.board)): 
	    	for y in range(len(self.board[x])): 
	    		print(self.board[x][y], end = '')
	    		if y == len(self.board[x])-1: 
	    			print()
	    		else:
	    			print('|', end = '')

class Player1: 
	def __init__(self, gameboard, playstyle): 
		

if __name__ == "__main__":

	print("starting")
	gameboard = Gameboard(20)
	gameboard.update()