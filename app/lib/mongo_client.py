''' This file contains mongodbclient class definition '''
import pymongo
from app.lib.singleton import Singleton
from app.lib.env import Env

class MongoClient(metaclass = Singleton): # pragma: no cover
  ''' This class implements mongo db client '''
  def __init__(self):
    print(f'{self.__connection_string=}')
    self.client = pymongo.MongoClient(self.__connection_string)
    self.database = self.client[self.__mongo_database_name]
    self.collection = self.database['collection']

  def check_connection(self):
    ''' Checks mongodb connection '''
    return self.client.server_info()['version'] is not None

  @property
  def __connection_string(self):
    ''' Returns connection string '''
    return f"mongodb://{self.__auth_string}{self.__mongo_host}"

  @property
  def __auth_string(self) -> str:
    ''' Returns authentication string '''
    return f"{self.__mongo_user_name}:{self.__mongo_password}@"

  @property
  def __mongo_user_name(self) -> str:
    ''' Returns mongodb user name '''
    return Env().get('MONGO_USER_NAME')

  @property
  def __mongo_password(self) -> str:
    ''' Returns mongodb user passord '''
    return Env().get('MONGO_USER_PASSWORD')

  @property
  def __mongo_database_name(self) -> str:
    ''' Returns mongodb database name '''
    return Env().get('MONGO_DATABASE_NAME')

  @property
  def __mongo_host(self) -> str:
    ''' Returns mongodb host '''
    return Env().get('MONGO_HOST')
