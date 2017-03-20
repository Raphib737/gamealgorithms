from player import Player
from functools import reduce

"""
Computer Class which is used to Computer program in the game.
This inherits the player class and modifies its make_move function
This computer implements the xor strategy to determine how many sticks it needs to remove
"""
class Computer(Player):
	name = ""

	def __init__(self,name):
		self.name = name

	def make_move(self,board):
		"""
			This method takes in a board object and creates a new temp board removing sticks from it until the boards xor value
			is 0.

			Args:
				Param 1: board Object

			Returns:
				None
		"""
		
		num_set = []
		for key in sorted(board.board.keys()):
			num_set.append(board.board[key]);

		num_set_copy = num_set[:]  #Shallow copy so values arent shared and list can be resetted

		nim_sum = 1;
		first_pass = True;
		row = 0
		while(nim_sum != 0):
			num_set = num_set_copy[:];
			if(first_pass):
				num_sticks_to_remove = num_set[row]
				first_pass = False
			else:
				num_sticks_to_remove = num_sticks_to_remove - 1
			
			if(num_sticks_to_remove < 1):
				row +=1;
				num_sticks_to_remove = num_set[row];
				first_pass = True
			else:
				num_set[row] = num_set[row] - num_sticks_to_remove;
				nim_sum = reduce(int.__xor__,num_set);

		board.board["row_"+str(row+1)] = board.board["row_"+str(row+1)] - num_sticks_to_remove
		print(self.name + " removed " + str(num_sticks_to_remove) + " stick(s) from row " + str(row+1)+ ".")