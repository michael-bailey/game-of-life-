'''
Wave function.

This explores the wavefunction copllapse algorithm
'''

from SudokuBoard import SudokuBoard

def main():
	'''main function'''
	print("Hello world")
	board = SudokuBoard.load("board.csv")
	print(board)
	print(board.get_row(2))
	print(board.get_col(2))
	print(board.get_square(1,2))

if __name__ == "__main__":
	main()
