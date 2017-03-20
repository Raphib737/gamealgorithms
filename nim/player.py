import os
from functools import reduce

"""
Player Class which is used to depict a player in the game.
Only contains 1 attribute which is the name of the player.
"""
class Player():

	name = ""

	def __init__(self,name):
		self.name = name;

	def make_move(self,board):
		"""
			This function takes in a board object and makes a move from it and prints out
			to the console the move that the player did.

			Args:
				Param 1: board Object

			Returns:
				None
		"""
		selected_row = eval(input("Select a Row to remove from: "));
		num_sticks = eval(input("Select how many sticks you will remove in row " + str(selected_row) +": "));

		error_message = board.valid_move(selected_row,num_sticks);

		while(error_message != ""):  #Checks input to see if its a valid input, if not keep asking for a valid move
			print("\n********************")
			print(error_message);
			print("********************\n")
			selected_row = eval(input("Select a Row to remove from: "));
			num_sticks = eval(input("Select how many sticks you will remove in row " + str(selected_row) +": "));
			error_message = board.valid_move(selected_row,num_sticks);
		
		os.system('clear');           #Clears screen

		print("\n......................................................");
		print(self.name + " removed " + str(num_sticks) + " stick(s) from row " + str(selected_row));
		print("......................................................\n")
		
		board.board["row_"+str(selected_row)] = board.board["row_"+str(selected_row)] - num_sticks;
