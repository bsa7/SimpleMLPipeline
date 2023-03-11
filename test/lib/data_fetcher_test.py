''' This file contains unit tests for app/lib/data_fetcher.py '''
import unittest
import responses
from app.lib.data_fetcher import DataFetcher
from app.lib.api_exmo_client import ApiExmoClient
from app.lib.utils import current_timestamp, days, hours, seconds
from app.models.application_record import ApplicationRecord
from app.models.candle import Candle
from app.types.api_exmo_responses import CandlesHistory
from test.support.stub_helper import stub_get_request

class TestDataFetcher(unittest.TestCase):
  ''' This class contains tests for DataFetcher class '''
  def setUp(self):
    ''' Clean up after each test '''
    ApplicationRecord.collection.cleanup()

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

  def test_update_when_data_already_present(self):
    ''' This case checks the update method not query same data from API twice '''
    uri2 = 'https://api.exmo.com/v1.1/candles_history?from=1585551801&resolution=D&symbol=BTC_USDT&to=1585551900'
    expected_response2: CandlesHistory = { 'candles': [{ 't': 2 }] }
    instrument = 'BTC_USDT'
    Candle.insert_one(instrument = instrument, ds = 1585551800000, t = 3)
    data_fetcher = DataFetcher(api_client = ApiExmoClient(resolution = 'D'),
                               from_timestamp = 1583219100000,
                               to_timestamp = 1585551900000,
                               batch_size_in_milliseconds = days(25))

    with responses.RequestsMock() as rsps:
      stub_get_request(rsps, uri2, expected_response2)
      result = data_fetcher.update(symbol = instrument)
      self.assertEqual(result, expected_response2['candles'])

  def test_update_when_no_latest_timestamp_is_present(self):
    ''' This case checks the update method query data till current time '''
    current_time = current_timestamp()
    earlier_time = current_time - days(2)
    nearest_time = current_time - hours(2)

    time_from = int(nearest_time / 1000 + 1)
    time_to = int(current_time / 1000)
    uri2 = f'https://api.exmo.com/v1.1/candles_history?from={time_from}&resolution=D&symbol=BTC_USDT&to={time_to}'
    expected_response2: CandlesHistory = { 'candles': [{ 't': 2 }] }
    instrument = 'BTC_USDT'
    Candle.insert_one(instrument = instrument, ds = nearest_time, t = 3)
    data_fetcher = DataFetcher(api_client = ApiExmoClient(resolution = 'D'),
                               from_timestamp = earlier_time,
                               batch_size_in_milliseconds = days(25))

    with responses.RequestsMock() as rsps:
      stub_get_request(rsps, uri2, expected_response2)
      result = data_fetcher.update(symbol = instrument)
      self.assertEqual(result, expected_response2['candles'])
