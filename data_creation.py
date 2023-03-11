''' This file run methods for data creation '''
from app.lib.api_exmo_client import ApiExmoClient
from app.lib.data_fetcher import DataFetcher
from app.lib.utils import current_timestamp, days
from app.models.candle import Candle

from_timestamp = current_timestamp() - days(365)
data_fetcher = DataFetcher(api_client = ApiExmoClient(resolution = 'D'),
                           from_timestamp = from_timestamp,
                           to_timestamp = current_timestamp(),
                           batch_size_in_milliseconds = days(25))

INSTRUMENT_NAME = 'BTC_USDT'
result = data_fetcher.update(INSTRUMENT_NAME)

for item in result:
  timestamp = item['t']
  average_value = (item['o'] + item['c']) / 2
  Candle.upsert_one(find_by = { 'ds': timestamp, 'instrument': INSTRUMENT_NAME }, data = { 'y': average_value })
