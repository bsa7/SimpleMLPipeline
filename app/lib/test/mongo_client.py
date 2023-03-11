''' This file contains self-writed implementation for inmemory mongo client '''

class Collection:
  ''' This class contains emulation of mongodb collection '''
  __storage = []

  @classmethod
  def find_many(cls, filter_attributes):
    ''' Returns list of filtered documents '''
    def filter_lambda(item):
      return item.items() | filter_attributes.items() == item.items()

    result = filter(filter_lambda, cls.__storage)
    return list(result)

  @classmethod
  def count_documents(cls, filter_attributes) -> int:
    ''' Returns count of filtered documents '''
    return len(cls.find_many(filter_attributes))

  @classmethod
  def insert_one(cls, record_attributes):
    ''' Insert one record to storage '''
    return cls.__storage.append(record_attributes)

  @classmethod
  def find_one(cls, filter_attributes):
    ''' Find first record with exact attributes '''
    return cls.find_many(filter_attributes)[0]

  @classmethod
  def cleanup(cls):
    ''' Clears internal storage '''
    cls.__storage = []

class MongoClient:
  ''' This class implements mongo db client '''
  collection = Collection
