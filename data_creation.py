''' This file run methods for data creation '''
from app.lib.api_exmo_client import ApiExmoClient
from app.lib.data_fetcher import DataFetcher
from app.lib.utils import current_timestamp, days

from_timestamp = current_timestamp() - days(365)
data_fetcher = DataFetcher(api_client = ApiExmoClient(resolution = 'D'),
                           from_timestamp = from_timestamp,
                           to_timestamp = current_timestamp(),
                           batch_size_in_milliseconds = days(25))

result = data_fetcher.update('BTC_USDT')

print(f'{result=}')
