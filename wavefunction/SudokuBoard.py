from __future__ import annotations
from typing import List, Optional, Set
from csv import reader

import SudokuBoardDelegate


class SudokuBoard(object):
	'''
		SudokuBoard

		A representation of the sudoku board.

		it has functions for fetching different rows columns and sub-squares

		This does not include the wave function probabilities.
	'''

	array: List[List[str]]
	__delegate: Optional['SudokuBoardDelegate.SudokuBoardDelegate']
	
	def __init__(self) -> None:
		self.array = [['_' for _ in range(1,10)] for _ in range(1,10)]

	def __str__(self) -> str:
		return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.array])

	def set_delegate(self, delegate: 'SudokuBoardDelegate.SudokuBoardDelegate'):
		self.__delegate = delegate
		self.__delegate.init_update(self)

	def get_row(self, index: int) -> List[str]:
		return self.array[index]

	def get_col(self, index: int) -> List[str]:
		return [x[index] for x in self.array]

	def get_square(self, col: int, row: int) -> List[List[str]]:
		col_index = 0 + (3*col)
		row_index = 0 + (3*row)
		return [self.array[i][row_index:row_index+3] for i in range(col_index, col_index+3)]

	def get_posibilities(self, row: int, col: int) -> Optional[Set[str]]:
		if self.__delegate == None: return None
		return self.__delegate.get_posibilities(row,col)
	
	def set_number(self, row: int, col: int, number: str):
		self.array[row][col] = number
		if self.__delegate != None: self.__delegate.cell_update(self, row, col)

	@staticmethod
	def load(filename: str) -> SudokuBoard:
		'''Loads a board form a file called "board.csv"'''
		with open(filename, 'r') as file:
			arr = [x for x in reader(file)]
			board = SudokuBoard()
			board.array = arr
			return board
		