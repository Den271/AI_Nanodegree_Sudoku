assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

# box is like 'A1' or 'B2'
boxes = cross(rows, cols)   #enumerate all boxes in A1-like form, i.e. A1, A2, ..., B1 ,B2, ... I9

# units - is the union of boxes
row_units = [cross(r, cols) for r in rows]      # [['A1', 'A2',...,'A9'],['B1', 'B2', ..., 'B9'],...,[...,'I9']]
column_units = [cross(rows, c) for c in cols]   #[[A1,B1,...,],...,[]]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')] # all square units
# let's add the diagonal units, 
# left-top to right-bottom diagonal: A1, B2, ..., I9
left_top_right_bottom_units= [r+c for r,c in zip(rows, cols)]
#left-bottom to right-top diagonal: A1, B2, ..., I9                 
left_bottom_right_top_units= [r+c for r,c in zip(rows[::-1], cols)]

unitlist = row_units + column_units + square_units + [left_top_right_bottom_units , left_bottom_right_top_units]

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

unitsRow = dict((s, [u for u in row_units if s in u]) for s in boxes)
peersRow = dict((s, set(sum(unitsRow[s],[]))-set([s])) for s in boxes)

unitsCol = dict((s, [u for u in column_units if s in u]) for s in boxes)
peersCol = dict((s, set(sum(unitsCol[s],[]))-set([s])) for s in boxes)

def grid_values(grid):
    """
        Convert grid into a dict of {square: char} with '123456789' for empties.
        Input: A grid in string form.
        Output: A grid in dictionary form
                Keys: The boxes, e.g., 'A1'
                Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    pairs_values = [box for box in values.keys() if len(values[box]) == 2] # limit the number of boxes to the
    for box in pairs_values:
        digit2 = values[box]
        #eliminate Row twins if any
        for peer1 in peersRow[box]:
            if values[peer1]==digit2 : #if naked twin found in a row peersRow[box]
                for peer2 in peersRow[box]:
                    if peer2!=peer1 : # for the rest of the row
                        values[peer2] = values[peer2].replace(digit2[0],'').replace(digit2[1],'')
        #eliminate Row twins if any
        for peer1 in peersCol[box]:
            if values[peer1]==digit2 : #if naked twin found in a col peersRow[box]
                for peer2 in peersCol[box]:
                    if peer2!=peer1 : # for the rest of the row
                        values[peer2] = values[peer2].replace(digit2[0],'').replace(digit2[1],'')
                        
    return values

    # Eliminate the naked twins as possibilities for their peers
    
    return values

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1] # limit the number of boxes to the
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)

        # Apply naked twins elimination,
        values = naked_twins(values) # elimnate naked twins

        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, try all possible values."
    
    values = reduce_puzzle(values) # First, reduce the puzzle using the previous function
    
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
