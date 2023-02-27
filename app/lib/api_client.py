''' This file contains class for fetch data from abstract API '''

from abc import ABC, abstractmethod
from app.types.api_exmo_responses import CandlesHistory
import requests

class ApiClient(ABC):
  ''' This class is wrapper for API classes '''

  @abstractmethod
  def _api_url(self) -> str:
    ''' Returns API url '''
    return ''

  @abstractmethod
  def fetch_data(self, symbol: str, from_timestamp: int, to_timestamp: int) -> CandlesHistory:
    ''' This common method name for api_client implementation. It load data portion from API '''
    return

  def fetch_data_in_batches(self,
                            symbol: str,
                            from_timestamp: int,
                            to_timestamp: int,
                            batch_size_in_milliseconds: int) -> CandlesHistory:
    ''' This common method name for api_client implementation. It load any volume of data in batches from API '''
    time_intervals = self.__time_intervals(from_timestamp, to_timestamp, batch_size_in_milliseconds)
    result: CandlesHistory = []
    for [start_timestamp, finish_timestamp] in time_intervals:
      result += self.fetch_data(symbol, from_timestamp = start_timestamp, to_timestamp = finish_timestamp)

    return result

  def _get(self, api_path: str, request_attributes: dict) -> dict:
    ''' This method implement GET request to API '''
    query: str = self.__query_string(request_attributes)
    uri: str = f'{self._api_url}{api_path}?{query}'
    response = requests.get(uri, timeout = 1)
    return response.json()

  def __time_intervals(self,
                       from_timestamp: int,
                       to_timestamp: int,
                       batch_size_in_milliseconds: int) -> list[list[int, int]]:
    ''' This method splits a large time interval into parts of a valid size '''
    intervals = [*range(from_timestamp, to_timestamp, batch_size_in_milliseconds), to_timestamp]
    zipped = zip(intervals[:-1], intervals[1:])
    return list(map(lambda x: [x[0] + 1, x[1]], zipped))


  def __query_string(self, attributes: dict) -> str:
    ''' Builds a query string for GET request '''
    query: list[str] = []
    for key in sorted(attributes.keys()):
      query.append(f'{key}={attributes[key]}')

    return '&'.join(query)
