''' This file contains unit tests for app/lib/utils.py '''
import unittest
from app.lib.utils import hours

class TestHours(unittest.TestCase):
  ''' This class runs all tests for hours method '''
  def test_hours_returns_zero(self):
    ''' This case checks the result for a valid zero timestamp '''
    self.assertEqual(hours(0), 0)

  def test_hours_returns_for_integer_argument(self):
    ''' This case checks the correct result for integer argument '''
    self.assertEqual(hours(11), 39600000)

  def test_hours_returns_for_float_argument(self):
    ''' This case checks the correct result for float argument '''
    self.assertEqual(hours(1.45), 5220000)
