''' This file contains unsorted methods '''
from datetime import datetime

def timestamp_to_formatted_datetime(timestamp: int) -> str:
  ''' Converts a unix timestamp with milliseconds (1585557000000) to formatted date like:
      2020-03-30 08:30:00.231000 '''
  return datetime.utcfromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')

def current_timestamp() -> int:
  ''' This method returns the current time in unix timestamp (in milliseconds) '''
  return int(datetime.now().timestamp() * 1000)

def seconds(value: float) -> int:
  ''' This method returns milliseconds for value of seconds '''
  return int(value * 1000)

def minutes(value: float) -> int:
  ''' This method returns milliseconds for value of minutes '''
  return seconds(value * 60)

def hours(value: float) -> int:
  ''' This method returns milliseconds for value of hours '''
  return minutes(value * 60)

def days(value: float) -> int:
  ''' This method returns milliseconds for value of days '''
  return hours(value * 24)
