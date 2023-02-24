''' This file contains unsorted methods '''
from datetime import datetime

def timestamp_to_formatted_datetime(timestamp: int) -> str:
  ''' Converts a unix timestamp with milliseconds (1585557000000) to formatted date like:
      2020-03-30 08:30:00.231000 '''
  return datetime.utcfromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
