'''
	SudokuCellSuperposition.py
'''

from typing import List, Set, Optional
from xmlrpc.client import Boolean

class SudokuCellSuperposition(object):
	'''
		SudokuCellSuperposition
	'''

	posibilities: Set[str]
	value: Optional[str]

	row: List['SudokuCellSuperposition']
	col: List['SudokuCellSuperposition']
	square: List['SudokuCellSuperposition']

	def __init__(self) -> None:
		self.posibilities = set([str(x) for x in range(1,10)])
		self.value = None

		self.row = []
		self.col = []
		self.square = []

	def collapse(self, number: str):
		self.posibilities = set()
		self.value = number

		for item in self.row:
			item.remove_possibility(number)

		for item in self.col:
			item.remove_possibility(number)

		for item in self.square:
			item.remove_possibility(number)

	def remove_possibility(self, number: str):
		self.posibilities.discard(number)
		if len(self.posibilities) == 1:
			self.collapse(list(self.posibilities)[0])
			

	def get_entropy(self) -> int:
		return len(self.posibilities)
	
	def is_collapsed(self) -> bool:
		return self.value != None
