# Game of Nim
Nim is a two player game where you can either play with a friend or go up against my very challenging computer. 

When you start the game, a random number of piles consisting of a random number of stones is created.

Each players take turns removing stones from only 1 pile of their choice. You can remove as many stones as you would like from the pile you select.

The winner is the last person who took the last set of stones from the last pile.

To Run the Program:
``` sh
>> python3 nim.py
```

## Files
### nim.py
This program is the heart of the program. This contains printing out the menu and controlling the navigation of the application
### board.py
This class is responsible for storing the state of the game as well as sanitize any invalid inputs the user has when playing the game. The data structure holding the state of the game is a dictionary/map.
### player.py
This class is for holding the information of the players who are playing the game, specifically their string name as well as allows them to make a move on the board
### computer.py
This class inherits the player class and overrides its make_move() function. This class is used for the 1 player section of the game.


## Algorithm behind the Computer
The algorithm implemented for the computer is based off the most using the bit operation or on the # of sticks on each row. From there if it ever equals 0, then we are in a terminal position which means that no matter what move the next player makes, we can always go back to a position which is considered the "Winning Move". more info can be found in the CMU game theory book and my NP calculator: [Game Theory Book](http://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/comb.pdf) and [np-calculator github](https://github.com/Raphib737/gamealgorithms/blob/master/np/npCalculator.py)





