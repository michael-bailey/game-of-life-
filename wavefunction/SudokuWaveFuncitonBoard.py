'''
	SudokuWaveFuncitonBoard.py
'''

from typing import List
import SudokuBoard
import SudokuBoardDelegate
import SudokuCellSuperposition


class SudokuWaveFuncitonBoard(SudokuBoardDelegate.SudokuBoardDelegate):

	__array: List[List['SudokuCellSuperposition.SudokuCellSuperposition']]

	def __init__(self) -> None:
		super().__init__()
		self.__array = [[SudokuCellSuperposition.SudokuCellSuperposition() for _ in range(0,10)] for _ in range(0,10)]

	def cell_update(self, board: 'SudokuBoard.SudokuBoard', row: int, col: int):
		print("[SudokuWaveFuncitonBoard:cell_update] row:{} col:{}", row,col)

	def init_update(self, board: 'SudokuBoard.SudokuBoard'):
		print("[SudokuWaveFuncitonBoard:init_update]")
		for (r_index, row) in enumerate(board.__array):
			for (c_index, col) in enumerate(row):
				match col:
					case "_":
						continue
					case r"[0-9]":
						self.collapse(r_index,c_index, col)
						
	def collapse(self, row: int, col: int, number: str):
		self.__array[row][col].collapse(number)
		raise NotImplementedError()
	