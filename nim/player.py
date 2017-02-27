import os
from functools import reduce

class Player():
	name = ""

	def __init__(self,name):
		self.name = name;

	def make_move(self,board):
		selected_row = eval(input("Select a Row to remove from: "));
		num_sticks = eval(input("Select how many sticks you will remove in row " + str(selected_row) +": "));

		error_message = board.valid_move(selected_row,num_sticks);
		while(error_message != ""):
			print("\n********************")
			print(error_message);
			print("********************\n")
			selected_row = eval(input("Select a Row to remove from: "));
			num_sticks = eval(input("Select how many sticks you will remove in row " + str(selected_row) +": "));
			error_message = board.valid_move(selected_row,num_sticks);
		os.system('clear');
		print("\n......................................................");
		print(self.name + " removed " + str(num_sticks) + " stick(s) from row " + str(selected_row));
		print("......................................................\n")
		board.board["row_"+str(selected_row)] = board.board["row_"+str(selected_row)] - num_sticks;
