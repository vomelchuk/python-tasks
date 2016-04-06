import unittest
from exersize2 import *

class Task2TestCase(unittest.TestCase):
	"""Tests for `exersize2.py`"""

	def test_is_list_get_real_result(self):
		self.assertEqual(getMaxMinAvg([1,2,3]), {'max':3, 'min':1, 'avg':2}, msg='Error!')

	def test_function_isPalindrom(self):
		# list of palindroms
		palindrom = ['abcdDCba', 'Мёд ждём!', 'Ила дикарю раки дали.', 'Там холм лохмат.']
		for item in palindrom:
			self.assertTrue(isPalindrom(item))
		# list of no palindroms
		nopalindrom = ['Home', 'I am batman', 'Vitaliy']
		for item in nopalindrom:
			self.assertFalse(isPalindrom(item))
	
	def test_function_reverse_string(self):
		self.assertEqual(reverseString("Home"), "emoH", msg="Error")
		self.assertEqual(reverseString("0123456789"), "9876543210", msg="Error")
		self.assertEqual(reverseString("My name`s Vitaliy"), "yilatiV s`eman yM", msg="Error")

if __name__ == '__main__':
	unittest.main()