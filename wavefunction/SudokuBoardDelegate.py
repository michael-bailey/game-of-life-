'''
	SudokuBoardDelegate.py
'''

from abc import abstractmethod
import SudokuBoard
from typing import List, Set

from SudokuCellSuperposition import SudokuCellSuperposition

class SudokuBoardDelegate(object):

	@abstractmethod
	def cell_update(self, board: 'SudokuBoard.SudokuBoard', row: int, col: int):
		raise NotImplementedError()

	@abstractmethod
	def init_update(self, board: 'SudokuBoard.SudokuBoard'):
		raise NotImplementedError()

	@abstractmethod
	def get_posibilities(self, row: int, col: int) -> Set:
		raise NotImplementedError()

	@abstractmethod
	def get_entropy(self, row: int, col: int) -> int:
		raise NotImplementedError()

	def get_lowest_entropys(self) -> List[SudokuCellSuperposition]:
		raise NotImplementedError()