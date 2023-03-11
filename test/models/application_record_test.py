''' This file contains test for Candle model tests '''
import unittest
from app.models.application_record import ApplicationRecord
from app.models.candle import Candle

class TestApplicationRecord(unittest.TestCase):
  ''' This class contains tests for base methods of Candle::ApplicationRecord model class '''

  def tearDown(self):
    ''' Clean up after each test '''
    ApplicationRecord.collection.cleanup()

  def test_zero_count(self):
    ''' This case checks if model can get correct zero count when no record exists '''
    count = Candle.count()
    self.assertEqual(count, 0)

  def test_count(self):
    ''' This case checks if model can get correct zero count when some records are exists '''
    Candle.insert_one(ds = 123456, y = 123)
    Candle.insert_one(ds = 123457, y = 124)
    self.assertEqual(Candle.count(), 2)

  def test_insert_one(self):
    ''' This case checks if model correctly insert one record '''
    record_search_attributes = { 'ds': 12345 }
    record_attributes = { 'y': 123 }
    expected_record_attributes = { 'model': 'Candle', **record_search_attributes, **record_attributes }
    Candle.insert_one(**record_search_attributes, **record_attributes)
    created_record = Candle.find_one(**record_search_attributes)
    self.assertEqual(created_record, expected_record_attributes)
