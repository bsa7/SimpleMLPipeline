''' This file contains a DataFetcher class - this class working with data: load data, store data '''
from app.models.candle import Candle
from app.lib.utils import current_timestamp, minutes

class DataFetcher():
  ''' This class fetches new portion of data from desired source. '''
  DEFAULT_FETCH_INTERVAL = minutes(1)

  def __init__(self,
               api_client,
               from_timestamp = None,
               to_timestamp = None,
               batch_size_in_milliseconds = DEFAULT_FETCH_INTERVAL):
    self.__from_timestamp = from_timestamp
    self.__to_timestamp = to_timestamp
    self.__api_client = api_client
    self.__batch_size_in_milliseconds = batch_size_in_milliseconds

  def update(self, symbol: str):
    ''' This method look over previous stored data and fetch new data '''
    start_timestamp = self.__start_timestamp(symbol)
    return self.__api_client.fetch_data_in_batches(symbol = symbol,
                                                   from_timestamp = start_timestamp,
                                                   to_timestamp = self.__finish_timestamp,
                                                   batch_size_in_milliseconds = self.__batch_size_in_milliseconds)

  def __start_timestamp(self, symbol: str) -> int:
    ''' This method determines the last point in time beyond which the required
        data is stored in the system. In fact, this moment plus one millisecond
        is the start for the time interval for which the data will be received. '''
    # In this point we would to find last data of time series in our db
    if Candle.count(instrument = symbol) == 0:
      return self.__from_timestamp

    oldest_existing_record = Candle.get_oldest(instrument = symbol).limit(1).next()
    oldest_timestamp = oldest_existing_record['ds']
    if oldest_timestamp > self.__from_timestamp:
      return self.__from_timestamp

    latest_existing_record = Candle.get_latest(instrument = symbol).limit(1).next()
    latest_timestamp = latest_existing_record['ds']

    return latest_timestamp + 1

  @property
  def __finish_timestamp(self) -> int:
    ''' This method always returns current timestamp '''
    if self.__to_timestamp is not None:
      return self.__to_timestamp

    return current_timestamp()
