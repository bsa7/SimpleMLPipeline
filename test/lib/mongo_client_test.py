''' This file contains unit tests for mongo client class instance '''
import unittest
from app.lib.service_factory import ServiceFactory

class TestMongoClient(unittest.TestCase):
  ''' This class contains unit tests for mongo client '''
  def setUp(self):
    self.__collection = ServiceFactory().mongo_client().collection

  def test_insert_one(self):
    ''' This case checks if the mongo client inserts one record to collection '''
    expected_document = { '_id': 'id-100500' }
    self.__collection.insert_one(expected_document)
    result = self.__collection.find_one(expected_document)
    self.assertEqual(expected_document, result)

  def test_read_collection_size(self):
    ''' This case checks the mongo client receive correct size of collection '''
