''' This file contains Candle model class definition '''
from app.models.application_record import ApplicationRecord

class Candle(ApplicationRecord):
  '''This class contains Candle class definition'''
  @classmethod
  def get_latest(cls, instrument: str) -> dict:
    ''' Returns latest record for desired instrument or None if no records found '''
    return cls.where(instrument = instrument).sort([('ds', -1)]).limit(1)

  @classmethod
  def get_oldest(cls, instrument: str) -> dict:
    ''' Returns oldest record for desired instrument or None if no records found '''
    return cls.where(instrument = instrument).sort([('ds', 1)]).limit(1)
