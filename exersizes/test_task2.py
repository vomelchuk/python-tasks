import unittest
from get_max_min_avg import getMaxMinAvg

class Task2TestCase(unittest.TestCase):
	"""Tests for `task2.py`"""

	def test_is_list_get_real_result(self):
		self.assertEqual(getMaxMinAvg([1,2,3]), {'max':3, 'min':1, 'avg':2}, msg='Error!')

if __name__ == '__main__':
	unittest.main()