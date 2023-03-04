''' This file contains unit tests for app/lib/utils.py '''
import unittest
from app.lib.utils import days

class TestDays(unittest.TestCase):
  ''' This class runs all tests for days method '''
  def test_days_returns_zero(self):
    ''' This case checks the result for a valid zero timestamp '''
    self.assertEqual(days(0), 0)

  def test_days_returns_for_integer_argument(self):
    ''' This case checks the correct result for integer argument '''
    self.assertEqual(days(11), 950400000)

  def test_days_returns_for_float_argument(self):
    ''' This case checks the correct result for float argument '''
    self.assertEqual(days(1.45), 125280000)
