''' This file contains implementation of ServiceFactory class '''
from app.lib.singleton import Singleton
from app.lib.env import Env
from app.lib.mongo_client import MongoClient
from app.lib.test.mongo_client import MongoClient as TestMongoClient

class ServiceFactory(metaclass = Singleton):
  ''' This class produces client classes for various services  '''
  @property
  def mongo_client(self):
    ''' Returns class for mongo_client '''
    return self.__client_by_env_name(production = MongoClient, test = TestMongoClient)

  def __client_by_env_name(self, development = None, production = None, test = None):
    ''' Returns one from given attributes depending on env name '''
    env_name = Env().name
    print(f'{env_name=}')
    if env_name == 'test':
      return test or development or production

    if env_name == 'development':
      return development or production

    return production or development
