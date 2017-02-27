from player import Player

class Computer(Player):
	name = ""

	def __init__(self,name):
		self.name = name

	def make_move(self,board):
		num_set = []
		for key in sorted(board.board.keys()):
			num_set.append(board.board[key]);
		
		num_set_copy = num_set
		nim_sum = 1;
		num_sticks_to_remove = 0;
		row = 0;
		first_pass = True;

		while(nim_sum != 0):
			row = num_set.index(max(num_set))
			if(first_pass):
				num_sticks_to_remove = num_set[row]
			else:
				num_sticks_to_remove = num_sticks_to_remove - 1
			
			num_set[row] = num_set[row] - num_sticks_to_remove;
			nim_sum = reduce(int.__xor__,num_set);

		board.board["row_"+str(row+1)] = board.board["row_"+str(row+1)] - num_sticks_to_remove
		print(self.name + " removed " + str(num_sticks_to_remove) + " stick(s) from row " + str(row+1)+ ".")