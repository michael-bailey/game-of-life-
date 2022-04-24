'''
Wave function.

This explores the wavefunction copllapse algorithm
'''

from SudokuBoard import SudokuBoard
from SudokuWaveFuncitonBoard import SudokuWaveFuncitonBoard
from random import choice

def main():
	'''main function'''
	print("Hello world")
	board = SudokuBoard.load("board.csv")
	superBoard = SudokuWaveFuncitonBoard()
	board.set_delegate(superBoard)
	print("---| start |---")
	print(board)

	print("---| iteration: {} |---".format(1))
	lowest = superBoard.get_lowest_entropys()
	chosen = choice(lowest)
	posibilities = list(chosen[0].posibilities)
	number = choice(posibilities)

	board.set_number(chosen[1], chosen[2], number)

	print(board)

	while True:
		print()
		lowest = superBoard.get_lowest_entropys()
		if len(lowest) == 0: break
		chosen = choice(lowest)
		posibilities = list(chosen[0].posibilities)
		number = choice(posibilities)

		board.set_number(chosen[1], chosen[2], number)

		print(board)

if __name__ == "__main__":
	main()
