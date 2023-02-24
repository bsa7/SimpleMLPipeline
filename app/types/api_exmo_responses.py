''' This file contains python types definitions for exmo API responses '''
from typing import TypedDict

class Candle(TypedDict):
  ''' This class defines a 'candle' item of candle history data '''
  t: int
  o: float
  c: float
  h: float
  l: float
  v: float

CandlesHistory = list[Candle]
