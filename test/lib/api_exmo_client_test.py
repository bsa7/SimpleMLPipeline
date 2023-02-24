''' This file contains unit tests for app/lib/api_exmo_client.py '''
import unittest
import responses
from app.types.api_exmo_responses import CandlesHistory
from app.lib.api_exmo_client import ApiExmoClient

class TestApiExmoClient(unittest.TestCase):
  ''' This class run all tests for ApiExmoClient class '''
  def test_candles_history_request_with_valid_params(self):
    ''' This case checks the situation when a regular response comes from api
        with correct request parameters '''
    uri = 'https://api.exmo.com/v1.1/candles_history?from=1585551900&resolution=1&symbol=BTC_USDT&to=1585552000'
    expected_response: CandlesHistory = { 'candles': [{ 't': 1 }] }
    with responses.RequestsMock() as rsps:
      self.__stub_get_request(rsps, uri, expected_response)
      response = ApiExmoClient().candles_history('BTC_USDT', 1585551900, 1585552000)
      self.assertEqual(response, expected_response['candles'])

  def __stub_get_request(self, rsps, api_uri: str, response: dict):
    ''' This method creates a stub for a specific api endpoint and emulates a
        successful data fetch '''
    rsps.get(api_uri, json = response, status = 200)
