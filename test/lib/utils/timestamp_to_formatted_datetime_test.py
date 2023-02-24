''' This file contains unit tests for app/lib/utils.py '''
import unittest
from app.lib.utils import timestamp_to_formatted_datetime

class TestTimestampToFormattedDatetime(unittest.TestCase):
  ''' This class runs all tests for timestamp_to_formatted_datetime method '''
  def test_result_with_valid_parameter(self):
    ''' This case checks the result for a valid timestamp parameter '''
    self.assertEqual(timestamp_to_formatted_datetime(1585557000231), '2020-03-30 08:30:00.231000')

  def test_result_when_parameter_is_none(self):
    ''' This case checks the raises for a None timestamp parameter '''
    self.assertRaises(TypeError, lambda: timestamp_to_formatted_datetime(None))

  def test_result_with_wrong_parameter(self):
    ''' This case checks the situation when the string parameter is specified incorrectly '''
    self.assertRaises(ValueError, lambda: timestamp_to_formatted_datetime(1585557000231121))
