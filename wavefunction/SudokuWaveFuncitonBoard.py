'''
	SudokuWaveFuncitonBoard.py
'''

from typing import List
import SudokuBoard
import SudokuBoardDelegate
import SudokuCellSuperposition


class SudokuWaveFuncitonBoard(SudokuBoardDelegate.SudokuBoardDelegate):

	__array: List[List['SudokuCellSuperposition.SudokuCellSuperposition']]

	def cell_update(self, board: 'SudokuBoard.SudokuBoard', row: int, col: int):
			return super().cell_update(board, row, col)