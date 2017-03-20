# Game of Nim
Nim is a two player game where you can either play with a friend or go up against my very challenging computer. 

When you start the game, a random number of piles consisting of a random number of stones is created.

Each players take turns removing stones from only 1 pile of their choice. You can remove as many stones as you would like from the pile you select.

The winner is the last person who took the last set of stones from the last pile.

To Run the Program:
``` sh
	>> python3 nim.py
```

## Algorithm behind the Computer
The algorithm implemented for the computer is based off the most using the bit operation or on the # of sticks on each row. From there if it ever equals 0, then we are in a terminal position which means that no matter what move the next player makes, we can always go back to a position which is considered the "Winning Move". more info can be found in my NP calculator found here: [Game Theory Book](http://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/comb.pdf) and [np-calculator github](https://github.com/Raphib737/gamealgorithms/blob/master/np/npCalculator.py)




