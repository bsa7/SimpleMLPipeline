''' This file contains test for Candle model tests '''
import unittest
from app.models.application_record import ApplicationRecord
from app.models.candle import Candle

class TestApplicationRecord(unittest.TestCase):
  ''' This class contains tests for base methods of Candle::ApplicationRecord model class '''

  def setUp(self):
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

  def test_upsert_one_when_no_record_exist(self):
    ''' This case checks if model correctly upser record when no desired record found '''
    record_search_attributes = { 'ds': 12345 }
    record_attributes = { 'y': 123 }
    expected_record_attributes = { 'model': 'Candle', **record_search_attributes, **record_attributes }
    existed_record = Candle.find_one(**record_search_attributes)
    self.assertEqual(existed_record, None)
    Candle.upsert_one(find_by = record_search_attributes, data = record_attributes)
    created_record = Candle.find_one(**record_search_attributes)
    self.assertEqual(created_record, expected_record_attributes)

  def test_upsert_one_when_same_record_exist(self):
    ''' This case checks if model correctly upser record when desired record has found '''
    record_search_attributes = { 'ds': 12345 }
    record_attributes = { 'y': 123 }
    new_record_attributes = { 'y': 125 }
    expected_existed_record_attributes = { 'model': 'Candle', **record_search_attributes, **record_attributes }
    expected_updated_record_attributes = { 'model': 'Candle', **record_search_attributes, **new_record_attributes }
    Candle.insert_one(**record_search_attributes, **record_attributes)
    existed_record = Candle.find_one(**record_search_attributes)
    self.assertEqual(existed_record, expected_existed_record_attributes)
    Candle.upsert_one(find_by = record_search_attributes, data = new_record_attributes)
    created_record = Candle.find_one(**record_search_attributes)
    self.assertEqual(created_record, expected_updated_record_attributes)
