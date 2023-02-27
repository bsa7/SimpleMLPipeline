''' This file contains client for time series database '''
from datetime import datetime
from app.lib.singleton import Singleton

class DbClient(Singleton):
  ''' This class contains client for database '''
  def __init__(self):
    ''' Initialize connection '''
    self.connection = None

  def find_latest_timestamp_for_symbol(self, symbol: str) -> dict:
    ''' This method finds the most recently stored value for a given pair and
        returns a timestamp of that value. '''
    result = {
      'symbol': symbol,
      'timestamp': datetime.now().timestamp() - 2 * 60000 # 2 minutes from now
    }

    return result
