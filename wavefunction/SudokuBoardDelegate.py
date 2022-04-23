
from abc import abstractmethod
import SudokuBoard


class SudokuBoardDelegate(object):

	@abstractmethod
	def cell_update(self, board: 'SudokuBoard.SudokuBoard', row: int, col: int):
		raise NotImplementedError()