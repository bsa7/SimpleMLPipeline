''' This file contains unit tests for app/lib/api_exmo_client.py '''
import unittest
import responses
from app.types.api_exmo_responses import CandlesHistory
from app.lib.api_exmo_client import ApiExmoClient
from test.support.mock_helper import stub_get_request

class TestApiExmoClient(unittest.TestCase):
  ''' This class contains tests for ApiExmoClient class '''
  def test_candles_history_request_with_valid_params(self):
    ''' This case checks the situation when a regular response comes from api
        with correct request parameters '''
    uri = 'https://api.exmo.com/v1.1/candles_history?from=1585551900&resolution=1&symbol=BTC_USDT&to=1585552000'
    expected_response: CandlesHistory = { 'candles': [{ 't': 1 }] }
    with responses.RequestsMock() as rsps:
      stub_get_request(rsps, uri, expected_response)
      response = ApiExmoClient().fetch_data('BTC_USDT', 1585551900, 1585552000)
      self.assertEqual(response, expected_response['candles'])
