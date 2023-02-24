''' This file run methods for data creation '''
from app.lib.api_exmo_client import ApiExmoClient
# from app.lib.utils import timestamp_to_formatteddatetime

# print(timestamp_to_formatteddatetime(1585557000000))

result = ApiExmoClient().candles_history('BTC_USDT', 1585551900, 1585552000)

print(f'{result=}')
