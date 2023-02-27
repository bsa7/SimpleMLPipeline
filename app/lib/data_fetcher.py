''' This file contains a DataFetcher class - this class working with data: load data, store data '''
from datetime import datetime
# from app.lib.env import Env

class DataFetcher():
  ''' This class fetches new portion of data from desired source. '''
  DEFAULT_FETCH_INTERVAL = 1 * 60000 # 1.minute

  def __init__(self,
               api_client,
               from_timestamp = None,
               to_timestamp = None,
               fetch_interval_size = DEFAULT_FETCH_INTERVAL):
    self.__from_timestamp = from_timestamp
    self.__to_timestamp = to_timestamp
    self.__api_client = api_client
    self.__fetch_interval_size = fetch_interval_size

  def update(self, symbol: str):
    ''' This method look over previous stored data and fetch new data '''
    start_timestamp = self.__start_timestamp(symbol)
    return self.__api_client.fetch_data_in_batches(symbol = symbol,
                                                   from_timestamp = start_timestamp,
                                                   to_timestamp = self.__finish_timestamp,
                                                   batch_size_in_milliseconds = self.__fetch_interval_size)

  def __start_timestamp(self, symbol: str) -> int:
    ''' This method determines the last point in time beyond which the required
        data is stored in the system. In fact, this moment plus one millisecond
        is the start for the time interval for which the data will be received. '''
    # In this point we would to find last data of time series in our db
    print(f'{symbol=}')
    if self.__from_timestamp is not None:
      return self.__from_timestamp

    return self.__finish_timestamp - self.__fetch_interval_size

  @property
  def __finish_timestamp(self) -> int:
    ''' This method always returns current timestamp '''
    if self.__to_timestamp is not None:
      return self.__to_timestamp

    return int(datetime.now().timestamp())
