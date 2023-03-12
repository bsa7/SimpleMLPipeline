''' This file contains Candle model class definition '''
from app.models.application_record import ApplicationRecord

class BestHyperparameter(ApplicationRecord):
  '''This class contains model for storing best hyper parameters '''

  @classmethod
  def get_latest(cls, ai_model: str) -> dict:
    ''' Returns latest record for desired instrument or None if no records found '''
    return cls.where(ai_model = ai_model).sort([('ds', -1)]).limit(1)
