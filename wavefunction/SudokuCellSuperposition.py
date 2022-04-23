'''
	SudokuCellSuperposition.py
'''

from typing import Set

class SudokuCellSuperposition(object):
	'''
		SudokuCellSuperposition
	'''

	__posibilities: Set[str]

	def __init__(self) -> None:
			self.__posibilities = Set([str(x) for x in range(0,10)])