''' This file contains unit tests for app/lib/utils.py '''
import unittest
from app.lib.utils import seconds

class TestSeconds(unittest.TestCase):
  ''' This class runs all tests for seconds method '''
  def test_seconds_returns_zero(self):
    ''' This case checks the result for a valid zero timestamp '''
    self.assertEqual(seconds(0), 0)

  def test_seconds_returns_for_integer_argument(self):
    ''' This case checks the correct result for integer argument '''
    self.assertEqual(seconds(11), 11000)

  def test_seconds_returns_for_float_argument(self):
    ''' This case checks the correct result for float argument '''
    self.assertEqual(seconds(1.45), 1450)
