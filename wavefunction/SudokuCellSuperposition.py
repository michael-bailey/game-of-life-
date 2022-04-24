'''
	SudokuCellSuperposition.py
'''

from typing import Set, Optional
from xmlrpc.client import Boolean

class SudokuCellSuperposition(object):
	'''
		SudokuCellSuperposition
	'''

	__posibilities: Set[str]
	__value: Optional[str]

	def __init__(self) -> None:
		self.__posibilities = set([str(x) for x in range(0,10)])
		self.__value = None

	def collapse(self, number: str):
		self.__posibilities = set()
		self.__value = number
	
	def remove_possibility(self, number: str):
		s = set([number])
		self.__posibilities = self.__posibilities.symmetric_difference(s)
	
	def is_collapsed(self) -> bool:
		return self.__value != None
