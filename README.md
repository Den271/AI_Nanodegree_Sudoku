# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Naked twins means that in Sudoku game state there are boxes in a Row/Column/or Block having the same possibilities. 
And the number of that possibilities(values) is two. 
So, it means that no such a values can be assigned in the rest of the corresponding Row or Column, this introduces the additional constraint propagation into the Depth First Search algorithm
The idea of solving the naked twins problem is to add the additional constraint propagation code:
	1) naked_twins(values) is implemented:
    	1.1) Find all possible instances of values of len==2, and for every candidate of len==2
    	1.2) if naked twins found in a row peersRow[box], then for the rest of the row, eliminate naked twin values
    	1.3) if naked twins found in a col peersCol[box], then for the rest of the column, eliminate naked twin values
    	1.4) Done
       1.5) It can be potentially be applied to the square_units both twins belong to
	2) it is called from reduce_puzzle(values) right after eliminate(values)
	3) So that after the implementing the constraints it search for naked twins in rows and columns, and if found, eliminates twins its values from the rest of the string or column

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Constraint propagation is the general term for propagating the implications CONSTRAINT PROPAGATION of a constraint on one variable onto other variables, in case of searching for the solution in Sudoku game parameter variables space.
The Sudoku goal searching algorithm is implemented using the Depth First Search strategy (DFS) in a tree of Sudoku game states. Constraint propagation is used to decrease the depth of recursion(or the number of itaretion) during search process.
Adding the constraints reduces the search space size, decreases the time and memory space required for the search.                                                                                         

Normal Sudoku game has three types of constraints:
    a. Row constraints
    b. Column constraints
    c. Block constraints
    And if the seach algo decides to apply the value into some block, then this step applies the new constraints to the other possiblities, eliminating them,  and the number of further search steps is reduced.
    So, more constraints we have propagate to the search space, lessier number of search recursion steps it can have.
    
    Diagonal sudoku problem has the two additional diagonal constraints to be propagated to reduce a search space:
    d. Diagonal constraints: All box values on the diagonal should be unique, there are two crossing diagonals in Sudoku table
    
    To add those diagonal Sudoku constraints into the algo, the two additional diagonal unit lists have been added into unitlist. 
        34: diagonal_units = [[r+c for r,c in zip(rows,cols)], [r+c for r,c in zip(rows,cols[::-1])]]
        36: unitlist = ... + diagonal_units
    This addition allows the eliminate(values) function to properly propagate the new diagonal constrains into the Sudoku states during the DFS search algorithm which reduces the execution time and space

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.