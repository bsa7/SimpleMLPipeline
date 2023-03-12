''' This file contains Collection class definition for mongo client testing class '''
from app.lib.test.cursor import Cursor
from app.lib.utils import filter_list

class Collection:
  ''' This class contains emulation of mongodb collection '''
  __storage = []

  @classmethod
  def find_many(cls, filter_attributes):
    ''' Returns list of filtered documents '''
    filter_lambda = filter_list(filter_attributes)
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
  def update_one(cls, filter_attributes, data_attributes):
    ''' Update one record in storage '''
    filter_lambda = filter_list(filter_attributes)
    record_index = list(map(filter_lambda, cls.__storage)).index(True)
    data = data_attributes['$set']
    cls.__storage[record_index] = { **cls.__storage[record_index], **data }

  @classmethod
  def update_many(cls, filter_attributes, data_attributes):
    ''' Update multiple records in storage '''
    filter_lambda = filter_list(filter_attributes)
    set_data = data_attributes.get('$set') or {}
    unset_data = data_attributes.get('$unset') or {}
    for index, item in enumerate(cls.__storage):
      if not filter_lambda(item):
        continue

      item = { **item, **set_data }
      for key in unset_data.keys():
        del item[key]
      cls.__storage[index] = item


  @classmethod
  def find_one(cls, filter_attributes):
    ''' Find first record with exact attributes '''
    result = cls.find_many(filter_attributes)
    if len(result) == 0:
      return None

    return result[0]

  @classmethod
  def cleanup(cls):
    ''' Clears internal storage '''
    cls.__storage = []

  @classmethod
  def find(cls, filter_attributes):
    ''' Returns Cursor instance for search results '''
    return Cursor(cls.find_many(filter_attributes))
