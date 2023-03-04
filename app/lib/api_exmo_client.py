''' This file contains class for fetch data from exmo API '''
from app.lib.api_client import ApiClient
from app.lib.env import Env
from app.types.api_exmo_responses import CandlesHistory

class ApiExmoClient(ApiClient):
  ''' This class contains methods for fetching data from API '''

  def fetch_data(self, symbol: str, from_timestamp: int, to_timestamp: int) -> CandlesHistory:
    ''' This method get candles of symbol from API for exact period '''
    request_attributes: dict = {
      'symbol': symbol,
      'from': int(from_timestamp / 1000),
      'to': int(to_timestamp / 1000),
      'resolution': self._resolution }

    result = self._get(self.__candles_history_path, request_attributes)
    return result['candles']

  @property
  def _api_url(self) -> str:
    ''' Returns exmo API url '''
    return Env().get('API_EXMO_HOST')

  @property
  def __candles_history_path(self) -> str:
    ''' Returns candles history API path '''
    return '/candles_history'
