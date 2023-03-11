''' This file contains ApplicationRecord abstract class definition '''
from app.lib.service_factory import ServiceFactory

class ApplicationRecord():
  ''' This abstract class contains base methods for data operation in mongo db '''
  collection = ServiceFactory().mongo_client().collection

  def __init__(self):
    ''' Initializes instance '''

  @classmethod
  def count(cls, **filter_attributes) -> int:
    ''' Returns count of model's records '''
    return cls.collection.count_documents({ 'model': cls.__name__, **filter_attributes })

  @classmethod
  def find_one(cls, **attributes):
    ''' find record by filter '''
    return cls.collection.find_one({ 'model': cls.__name__, **attributes })

  @classmethod
  def insert_one(cls, **record_attributes):
    ''' Insert one record model's records '''
    return cls.collection.insert_one({ 'model': cls.__name__, **record_attributes })

  @classmethod
  def upsert_one(cls, find_by, data):
    ''' Update existed or create new record '''
    existed_item = cls.find_one(**find_by)
    if existed_item is None:
      return cls.insert_one(**find_by, **data)

    print(f'{find_by=}, {data=}')
    return cls.collection.update_one({ 'model': cls.__name__, **find_by }, { '$set': data })