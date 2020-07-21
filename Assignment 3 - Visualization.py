  #Fern Exercise - Shell

'''
INSTRUCTIONS

This exercise will get you using control flows, and your artistic abilities to draw a fern.

At the end of the program, you need to have 2 lists, X and Y, containing the x and y coordinates for a number of dots.

The first set of coordinates is (0,0). Subsequent coordinates are generated from the previous coordinates according to the following rules:
- 1% of the time 
    + new X = 0
    + new Y = 0.16 * old Y
- 85% of the time 
    + new X = 0.85 * old X + 0.04 * old Y
    + new Y = -0.04 * old X + 0.85 * old Y + 1.6
- 7% of the time 
    + new X = 0.2 * old X - 0.26 * old Y
    + new Y = 0.23 * old X + 0.22 * old Y + 1.6
- 7% of the time 
    + new X = -0.15 * old X + 0.28 * old Y
    + new Y = 0.26 * old X + 0.24 * old Y + 0.44

- Your program should have a loop which adds the new coordinates to the lists (10k-100k is a good number of coordinates).
- Each iteration of the loop should call a function which returns the new coordiates
- After the loop, use the provided printImage function to display your coordinates.
'''

'''
Assignment 3 Reflection
Off the bat I was having a hard time conceptualizing where place the math statements which would be iterated through to graph the fern.  After the first ‘help along’ was given I was able to finish the code fairly quickly with some assistance at the end because I had written the math functions incorrectly but realized that after I had voiced my question.  
The biggest hang-up for me was not having the random number defined in the same function as the ‘tree’ of functions for the value of a given number.  Setting the initial coordinates for X and Y to 0 I also got but didn’t realize I needed to delete the random scatter plot from the X and Y definition in code provided.  Also, I learned a little about pylint while working through the code; it was helpful in case I misspelled variables.  
In learning the difference between tuples() vs. lists[], it was helpful to use both in the exercise.  We added to the list, as it was mutable, and did not add to the tuple.  
Another feature I learned after typing them out completely, was the find/replace feature in Visual Code.  This would have been very useful in replacing the old_x and old_y with the variable names I had defined.  
To really top the exercise off we could have used the dictionary, but the exercise was already complicated enough, and I believe we will be using dictionaries when we work with API’s in tomorrow’s class.  
'''

import matplotlib.pyplot as plt
import random


def newXY (x, y):
    """
    Generating new coordinates from the previous ones using a randomly generated number
    """

    temp_random = random.random()

    if temp_random<0.01:
        x_new= x
        y_new= 0.16*y
    elif temp_random<0.86:
        x_new= 0.85*x+0.04*y
        y_new= -0.04*x+0.85*y+1.6
    elif temp_random<0.93:
        x_new= 0.2*x-0.26*y
        y_new= 0.23*x+0.22*y+1.6
    else:
        x_new= -0.15*x+0.28*y
        y_new= 0.26*x+0.24*y+0.44

    return (x_new, y_new)

def printImage (X: list, Y: list):
    """
    Printing the image from lists of the x and y coordinates
    Args:
        X: list of x coordinates
        Y: list of y coordinates
    Returns:
        None
    Raises:
        None
    """
    plt.scatter(X, Y, c = "green", s = 1)
    plt.show()

def main():
#function to establish variables
    X = []
    Y = []
    X_coord = 0
    Y_coord = 0

    X.append(X_coord)
    Y.append(Y_coord)

    for i in range (100000):
        new_coord = newXY(X_coord, Y_coord)

        X_coord = new_coord[0]
        Y_coord = new_coord[1]

        X.append(X_coord)
        Y.append(Y_coord)

    printImage(X,Y)


if __name__ == "__main__":
  main()

