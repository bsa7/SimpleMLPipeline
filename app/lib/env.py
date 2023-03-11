''' This file contains Env class definition '''
import os
from dotenv import load_dotenv
from app.lib.singleton import Singleton

class Env(metaclass = Singleton):
  ''' This class implements get method for read environment variables. '''
  def __init__(self):
    load_dotenv()

  def get(self, variable_name: str):
    ''' This metod reads environment variable value '''
    return os.getenv(variable_name)

  @property
  def name(self) -> str:
    ''' Returns environment name (test | development | production) '''
    return os.getenv('PYTHON_ENV')
