#Done By Raphael Baysa
# Program to calculate N and P values and generate the board for a Take-away game
# npcalculator Class takes 2 parameters, the set of rules and the game size(# of items in the game to be taken away)
# 
#

class npCalculator:
	subtraction_set = [] #The available moves in the game
	target_num = 0       #The initial size of ur items (sticks,rocks etc...)
	np_board = {}				 #Generates a dictionary with key value pair of (#of items left, P or N)

	def __init__ (self, subtraction_set,target_num):
		self.subtraction_set = subtraction_set;
		self.target_num = target_num+1;
		self.fill_np_board();
	
	def fill_np_board(self):
		self.np_board = {0:'P'}

		for num in range(1,self.target_num):
			n_found = False
			for sub_numb in self.subtraction_set:
				if(num - sub_numb >= 0):	
					if(self.np_board[num-sub_numb] == 'P'):
						self.np_board[num] = 'N'
						n_found = True
						break;

			if(n_found == False):
				self.np_board[num] = 'P'
				n_found = False

	def printBoard(self):
		for keys in self.np_board:
			if(self.np_board[keys] == "P"):
				print(keys,self.np_board[keys])
		print(self.np_board)

def main():
	np = npCalculator([1,3,6],100)
	np.printBoard()

main()
			


