# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The idea of solving the naked twins problem is to add the additional constraint propagation code:
	1) naked_twins(values) is implemented
	1.1) Find all possible instances of values of len==2, and for every candidate of len==2
	1.2) if naked twins found in a row peersRow[box], then for the rest of the row, eliminate naked twin values
	1.3) if naked twins found in a col peersCol[box], then for the rest of the row, eliminate naked twin values
	1.4) Done
	2) it called from reduce_puzzle(values) right after eliminate(values)
	3) So that after the implementing the constraints it search for naked twins in rows and columns, and if found, eliminates twins its values from the rest of the string or column
	

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: To solve it, the two additional diagonal units sub-list have been added into unitlist. So that eliminate(values) function can use it to propagate constraints furthermore, including two diagonal constraint

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