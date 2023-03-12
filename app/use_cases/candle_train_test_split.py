''' This file contains use-case for generation pandas dataframes for train and/or test '''
import pandas as pd
from app.models.candle import Candle
from app.lib.utils import days, timestamp_to_formatted_date

class CandleTrainTestSplit:
  ''' This class split time series for desired candle to train and test sets '''
  def time_series_split_points(self, instrument_name: str):
    ''' Returns train and test dataframes '''
    latest_candle = Candle.get_latest(instrument = instrument_name).limit(1).next()
    latest_candle_timestamp = latest_candle.get('ds')
    latest_candle_date = timestamp_to_formatted_date(latest_candle_timestamp)
    oldest_candle = Candle.get_oldest(instrument = instrument_name).limit(1).next()
    oldest_candle_timestamp = oldest_candle.get('ds')
    oldest_candle_date = timestamp_to_formatted_date(oldest_candle_timestamp)
    splitting_timestamp = latest_candle_timestamp - days(30)
    splitting_date = timestamp_to_formatted_date(splitting_timestamp)

    return {
      'latest_candle': latest_candle,
      'latest_candle_timestamp': latest_candle_timestamp,
      'latest_candle_date': latest_candle_date,
      'oldest_candle': oldest_candle,
      'oldest_candle_timestamp': oldest_candle_timestamp,
      'oldest_candle_date': oldest_candle_date,
      'splitting_timestamp': splitting_timestamp,
      'splitting_date': splitting_date,
    }

  def load_data(self, instrument_name: str, train = True, test = True):
    ''' Load candles time series intor pandas DataFrame '''
    tp = self.time_series_split_points(instrument_name = instrument_name)
    df = pd.DataFrame({ 'ds': [], 'y': [], 'y_test': [], 'y_hat': [] })
    df.set_index('ds')

    # Fill the dataframe with train values
    if train:
      cursor = Candle.where(ds = { '$lt': tp['splitting_timestamp'] }).sort([('ds', 1)])
      train_df = pd.DataFrame(list(cursor))[['ds', 'y']]
      train_df.set_index('ds')
      df = pd.concat([df, train_df], axis = 0)
      df.set_index('ds')

    # Fill the dataframe with test values
    if test:
      cursor = Candle.where(ds = { '$gte': tp['splitting_timestamp'] }).sort([('ds', 1)])
      test_df = pd.DataFrame(list(cursor))[['ds', 'y']]
      test_df = test_df.rename(columns = { 'y': 'y_test' })
      test_df.set_index('ds')
      df = pd.concat([df, test_df], axis = 0)
      df.set_index('ds')

    return self.__map_datestamps(df)

  def __map_datestamps(self, df):
    ''' Convert unix timestamps to date YYYY-MM-DD '''
    df['ds'] = df['ds'].apply(timestamp_to_formatted_date)
    return df
