''' This file contains unit tests for mongo client class instance '''
import unittest
from mockupdb import going, MockupDB
from app.lib.mongo_client import MongoClient

class TestMongoClient(unittest.TestCase):
  ''' This class contains unit tests for mongo client '''
  def setUp(self):
    ''' Initializes mock server for mongodb client '''
    self.__server = MockupDB(auto_ismaster = True)
    self.__server.autoresponds('ismaster', maxWireVersion = 6)
    self.__server.run()
    self.addCleanup(self.__server.stop)
    self.__client = MongoClient(self.__server.uri)

  def test_insert_one(self):
    ''' This case checks if the mongo client inserts one record to collection '''
    expected_document = { '_id': 'id-100500' }
    with going(self.__client.database.collection.insert_one, expected_document) as future:
      self.__server.receives().ok()

    result = future()
    self.assertEqual('id-100500', result.inserted_id)

  def test_read_collection_size(self):
    ''' This case checks the mongo client receive correct size of collection '''
