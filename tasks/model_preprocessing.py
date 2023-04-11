''' This file contains step for data preprocessing
    All pre-processing of the data is that we find the average value between the
    opening and closing of the quote and save it in the same document with the key 'y'
'''

from app.models.candle import Candle

for item in Candle.where():
  open_value = item.get('o') or 0
  close_value = item.get('c') or 0
  y = (open_value + close_value) / 2
  ds = item.get('ds')
  if ds is not None:
    Candle.upsert_one(find_by = { 'ds': ds }, data = { 'y': y })
