''' This file contains SerializedTrainedModel model class definition '''
from app.models.application_record import ApplicationRecord
from app.lib.utils import current_timestamp

class TrainedModelSerialized(ApplicationRecord):
  '''This class contains model for storing serialized_model '''

  @classmethod
  def store(cls, model_name: str, instrument_name: str, model_data: dict):
    ''' This methods upsert model data by model name '''
    find_by = { 'ai_model': model_name, 'instrument_name': instrument_name }
    data = { 'json': model_data, 'ds': current_timestamp() }
    cls.upsert_one(find_by = find_by, data = data)

  @classmethod
  def restore(cls, model_name: str, instrument_name: str) -> dict:
    ''' This methods restore saved model data by model name '''
    result = cls.find_one(ai_model = model_name, instrument_name = instrument_name)
    if result is None:
      return None

    return result['json']
