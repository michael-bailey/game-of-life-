'''
	SudokuCellSuperposition.py
'''

from typing import List, Set, Optional
from xmlrpc.client import Boolean

class SudokuCellSuperposition(object):
	'''
		SudokuCellSuperposition
	'''

	__posibilities: Set[str]
	__value: Optional[str]

	row: List['SudokuCellSuperposition']
	col: List['SudokuCellSuperposition']
	square: List['SudokuCellSuperposition']

	def __init__(self) -> None:
		self.__posibilities = set([str(x) for x in range(0,10)])
		self.__value = None

		self.row = []
		self.col = []
		self.square = []

	def collapse(self, number: str):
		self.__posibilities = set()
		self.__value = number

		for item in self.row: item.remove_possibility(number)
		for item in self.col: item.remove_possibility(number)
		for item in self.square: item.remove_possibility(number)

	
	def remove_possibility(self, number: str):
		s = set([number])
		diff = self.__posibilities.symmetric_difference(s)
		self.__posibilities = diff
	
	def is_collapsed(self) -> bool:
		return self.__value != None
