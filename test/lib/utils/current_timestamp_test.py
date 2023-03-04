''' This file contains unit tests for app/lib/utils.py '''
import unittest
from datetime import datetime
from app.lib.utils import current_timestamp

class TestCurrentTimestamp(unittest.TestCase):
  ''' This class runs all tests for current_timestamp method '''
  def test_current_timestamp_returns_current_time(self):
    ''' This case checks the result for a valid timestamp '''
    expected_timestamp = int(datetime.now().timestamp() * 1000)
    self.assertEqual(current_timestamp(), expected_timestamp)
