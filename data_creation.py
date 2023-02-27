''' This file run methods for data creation '''
from app.lib.api_exmo_client import ApiExmoClient
from app.lib.data_fetcher import DataFetcher

data_fetcher = DataFetcher(api_client = ApiExmoClient(), fetch_interval_size = 60 * 1000)
result = data_fetcher.update('BTC_USDT')

print(f'{result=}')
