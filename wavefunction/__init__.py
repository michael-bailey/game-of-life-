'''
Wave function.

This explores the wavefunction copllapse algorithm
'''

from SudokuBoard import SudokuBoard
from SudokuWaveFuncitonBoard import SudokuWaveFuncitonBoard

def main():
	'''main function'''
	print("Hello world")
	board = SudokuBoard.load("board.csv")
	superBoard = SudokuWaveFuncitonBoard()
	board.set_delegate(superBoard)
	print(board)
	print(board.get_row(2))
	print(board.get_col(2))
	print(board.get_square(1,2))

	lowest = superBoard.get_lowest_entropys()
	print()

if __name__ == "__main__":
	main()
