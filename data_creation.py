''' This file run methods for data creation '''
from app.lib.api_exmo_client import ApiExmoClient
from app.lib.data_fetcher import DataFetcher
from app.lib.utils import current_timestamp, days
from app.models.candle import Candle

from_timestamp = current_timestamp() - days(2100)
data_fetcher = DataFetcher(api_client = ApiExmoClient(resolution = 'D'),
                           from_timestamp = from_timestamp,
                           batch_size_in_milliseconds = days(25))

INSTRUMENT_NAME = 'BTC_USDT'
result = data_fetcher.update(INSTRUMENT_NAME)

for item in result:
  timestamp = item['t']
  del item['t']
  Candle.upsert_one(find_by = { 'ds': timestamp, 'instrument': INSTRUMENT_NAME }, data = item)
