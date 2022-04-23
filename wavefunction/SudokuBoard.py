from __future__ import annotations
from typing import List
from csv import reader

import SudokuBoardDelegate


class SudokuBoard(object):
	'''
		SudokuBoard

		A representation of the sudoku board.

		it has functions for fetching different rows columns and sub-squares

		This does not include the wave function probabilities.
	'''

	__array: List[List[str]]
	

	def __init__(self) -> None:
		self.__array = [['_' for _ in range(0,10)] for _ in range(0,10)]

	def __str__(self) -> str:
		return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.__array])

	def set_delegate(self, delegate: 'SudokuBoardDelegate.SudokuBoardDelegate'):
		self.__delegate = delegate

	def get_row(self, index: int) -> List[str]:
		return self.__array[index]

	def get_col(self, index: int) -> List[str]:
		return [x[index] for x in self.__array]

	def get_square(self, col: int, row: int) -> List[List[str]]:
		col_index = 0 + (3*col)
		row_index = 0 + (3*row)
		return [self.__array[i][row_index:row_index+3] for i in range(col_index, col_index+3)]

	@staticmethod
	def load(filename: str) -> SudokuBoard:
		'''Loads a board form a file called "board.csv"'''
		with open(filename, 'r') as file:
			arr = [x for x in reader(file)]
			board = SudokuBoard()
			board.__array = arr
			return board
		