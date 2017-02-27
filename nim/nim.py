# Done By: Raphael Baysa U99595463
# How To Run: 'python3 nim.py' ***Only works on Python3****
# Basic game of Nim that implements nimsum algorithm on a computer class
# 
# Classes = [Player, Board, Computer(extends Player)]
# Board is represented as a dictionary with key -> row_n *n being an integer*
# # of rows of the board and sticks is generated randomly but can be changed in the Board class

# ****IF YOU ARE RUNNING ON A WINDOWS REPLACE ALL os.system('clear') WITH os.system('cls')****

from player import Player 
from board import Board
from computer import Computer

import os
import random

###### MAIN ########################
def main():
	os.system('clear');
	mode = print_main();
	while(mode!="q"):
		if(mode == 'a'):
			print_about();
			mode = print_main();
		elif(mode == "1" or mode == "2"):
			os.system('clear');
			board = Board();
			if(mode == "1"):
				board = Board();
				p1_turn = random.randint(10,100000) % 2 == 1
				p1_name = input("Enter player 1's name: ");
				p1 = Player(p1_name);
				p2 = Computer("Master Bot");
				
				while(not board.is_empty()):
					board.print_board();
					print("")
					if(p1_turn):
						print(p1.name + "'s turn")
						p1.make_move(board);
						p1_turn = False;
					else:
						print(p2.name + "'s turn")
						p2.make_move(board);
						p1_turn = True;
				if(p1_turn):
					print(p2.name + " has won!\n");
				else:
					print(p1.name + " has won!\n");

				p_again = input("Play again? (y/n): ")
				while(p_again != 'y' and p_again != 'n'):
					p_again = input("Not a valid input. Play Again? (y/n) : ")
				if(p_again == 'y'):
					mode = "1"
				else:
					os.system('clear');
					mode = print_main();

			elif (mode == "2"):
				p1_turn = True
				p1_name = input("Enter player 1's name: ");
				p1 = Player(p1_name);
				p2_name = input("Enter player 2's name: ");
				p2 = Player(p2_name);
				while(not board.is_empty()):
					board.print_board();
					print("")
					if(p1_turn):
						print(p1.name + "'s turn")
						p1.make_move(board);
						p1_turn = False;
					else:
						print(p2.name + "'s turn")
						p2.make_move(board);
						p1_turn = True;
				if(p1_turn):
					print(p2.name + " has won!\n");
				else:
					print(p1.name + " has won!\n");

				p_again = input("Play again? (y/n): ")
				while(p_again != 'y' and p_again != 'n'):
					p_again = input("Not a valid input. Play Again? (y/n) : ")
				if(p_again == 'y'):
					mode = "2"
				else:
					mode = print_main();

########## Generates the Main Menu Screen and returns a valid choice ##########
def print_main():
	print("Welcome to the Game Nim!\n");
	print("Main Menu");
	print("------------------------");
	print("a.) About/How to play");
	print("1.) Single-player");
	print("2.) Multiplayer");
	print("q.) Quit\n")

	possible_inputs = ['a','1','2','q'];

	mode = input("Enter Selection: ");

	while(mode not in possible_inputs):
		mode = input("invalid choice. Try again: ")
	return mode

########## Prints the About Page then the Main Menu again ##########
def print_about():
	os.system('clear');
	print("-------------------------------------------------");
	print("About")
	print("\nNim is a two player game. In this case, that means you and the computer. \n When you start the game, a random number of piles consisting of a random number of stones is put together. \nBoth players take turns. Each turn a player must remove one or more stones from a pile. \nThe player that takes the last stone(s) from the only remaining pile wins. Easy, eh?")
	print("-------------------------------------------------\n\n");

main()