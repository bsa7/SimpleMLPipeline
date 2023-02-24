''' This file contains unit tests for app/lib/env.py '''
import unittest
import os
from app.lib.env import Env

class TestEnv(unittest.TestCase):
  ''' This class contains tests for Env class '''
  def test_get_existed_environment_variable(self):
    ''' This case checks if Env.get can read environment variable value correctly '''
    expected_value = 'something'
    var_name = 'TEST_VARIABLE'
    os.environ[var_name] = expected_value
    self.assertEqual(Env().get(var_name), expected_value)
    os.environ.pop(var_name, None)

  def test_get_unexisted_environment_variable(self):
    ''' This case checks if Env.get read unexisted environment variable correctly '''
    expected_value = None
    var_name = 'TEST_VARIABLE'
    self.assertEqual(Env().get(var_name), expected_value)
