## Description
This is a Sudoku solver based on Backtracking.
It takes a custom puzzle as input and returns the solved puzzle

### Files:
* **board.py**: Conatins functions related to the sudoku board, printing, initialization
* **graph.py**: Contains a class graph which takes an adj matrix as input to create board
* **main.py**: contains main function to run program
* **soln.py**: Contains Backtracking Algorithm
* **render_p.py**: Renders the Gui on pygame _(in progress)_

### Running the Application
1) Clone the repository in your Local System using `git clone https://github.com/drishti307/sudoku.git`
2) Change directory in to Sudoku.py using cd command: `cd Sudoku.py`
3) Run following command on the terminal: `python main.py`

### Input Format:
Press 1 to give custom input, 2 to run algorithm on random 9x9 grid

### Input Format for Custom Input:
    i) Enter dimensions of board: 4, or 9, or 16....
    ii) Enter row, column and value of cell
    iii) To exit input system, enter any value greater than your dimensions

### Output
 Sudoku grid entered (before solving)
 Sudoku grid after it is solved
