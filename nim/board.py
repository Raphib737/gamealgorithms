import random

class Board():
	board = {}
	num_rows = 0

	def __init__(self):
		self.num_rows = random.randint(2,6);
		self.generate_board();

	def generate_board(self):
		for x in range(1,self.num_rows+1):
			self.board["row_"+str(x)]= random.randint(1,5);

	def print_board(self):
		print(self.board);

	def is_empty(self):
		for x in self.board.keys():
			if (self.board[x] != 0):
				return False
		return True

	def valid_move(self,row,num_sticks):
		if(self.num_rows < row or row < 1):
			return "Invalid row Selection";
		elif(num_sticks < 1 or num_sticks > self.board["row_"+str(row)]):
			return "Invalid number of sticks picked";
		else:
			return "";

	def print_board(self):
		print("-----------------------------")
		print("Game Board")
		print("-----------")
		for key in sorted(self.board.keys()):
			print(key + ": ",end="");
			print(self.board[key],end="");
			print(" sticks");
		print("-----------------------------")
