''' This file contains unit tests for app/lib/data_fetcher.py '''
import unittest
import responses
from app.lib.data_fetcher import DataFetcher
from app.lib.api_exmo_client import ApiExmoClient
from app.lib.utils import days, seconds
from app.types.api_exmo_responses import CandlesHistory
from test.support.mock_helper import stub_get_request

class TestDataFetcher(unittest.TestCase):
  ''' This class contains tests for DataFetcher class '''
  def test_update_with_default_resolution(self):
    ''' This case runs the Update method to ensure that the third party API
        call is being made and that the data received from both requests is
        being accumulated. '''
    uri1 = 'https://api.exmo.com/v1.1/candles_history?from=1585551901&resolution=1&symbol=BTC_USDT&to=1585551910'
    uri2 = 'https://api.exmo.com/v1.1/candles_history?from=1585551911&resolution=1&symbol=BTC_USDT&to=1585551920'
    expected_response1: CandlesHistory = { 'candles': [{ 't': 1 }] }
    expected_response2: CandlesHistory = { 'candles': [{ 't': 2 }] }
    data_fetcher = DataFetcher(api_client = ApiExmoClient(resolution = 1),
                               from_timestamp = 1585551900000,
                               to_timestamp = 1585551920000,
                               batch_size_in_milliseconds = seconds(10))

    with responses.RequestsMock() as rsps:
      stub_get_request(rsps, uri1, expected_response1)
      stub_get_request(rsps, uri2, expected_response2)
      result = data_fetcher.update(symbol = 'BTC_USDT')
      self.assertEqual(result, expected_response1['candles'] + expected_response2['candles'])

  def test_update_with_long_resolution(self):
    ''' This case runs the Update method to ensure that the third party API
        call is being made and that the data received from both requests is
        being accumulated. Also, resolution of candles is a days '''
    uri1 = 'https://api.exmo.com/v1.1/candles_history?from=1583219101&resolution=D&symbol=BTC_USDT&to=1585379100'
    uri2 = 'https://api.exmo.com/v1.1/candles_history?from=1585379101&resolution=D&symbol=BTC_USDT&to=1585551900'
    expected_response1: CandlesHistory = { 'candles': [{ 't': 1 }] }
    expected_response2: CandlesHistory = { 'candles': [{ 't': 2 }] }
    data_fetcher = DataFetcher(api_client = ApiExmoClient(resolution = 'D'),
                               from_timestamp = 1583219100000,
                               to_timestamp = 1585551900000,
                               batch_size_in_milliseconds = days(25))

    with responses.RequestsMock() as rsps:
      stub_get_request(rsps, uri1, expected_response1)
      stub_get_request(rsps, uri2, expected_response2)
      result = data_fetcher.update(symbol = 'BTC_USDT')
      self.assertEqual(result, expected_response1['candles'] + expected_response2['candles'])
