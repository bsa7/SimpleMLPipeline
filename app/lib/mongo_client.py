''' This file contains mongodbclient class definition '''
import pymongo
from app.lib.singleton import Singleton
from app.lib.env import Env

class MongoClient(metaclass = Singleton):
  ''' This class implements mongo db client '''
  def __init__(self, connection_url = None):
    url = connection_url or self.__connection_string
    self.client = pymongo.MongoClient(url)
    self.database = self.client[self.__mongo_database_name()]

  def check_connection(self):
    ''' Checks mongodb connection '''
    return self.client.server_info()['version'] is not None

  def collection(self, collection_name: str):
    ''' Returns collection by its name '''
    return self.database[collection_name]

  @property
  def __connection_string(self):
    ''' Returns connection string '''
    return f"mongodb://{self.__mongo_user_name()}:{self.__mongo_password()}@{self.__mongo_host()}"

  def __mongo_user_name(self):
    ''' Returns mongodb user name '''
    return Env().get('MONGO_USER_NAME')

  def __mongo_password(self):
    ''' Returns mongodb user passord '''
    return Env().get('MONGO_USER_PASSWORD')

  def __mongo_database_name(self):
    ''' Returns mongodb database name '''
    return Env().get('MONGO_DATABASE_NAME')

  def __mongo_host(self):
    ''' Returns mongodb host '''
    return Env().get('MONGO_HOST')
