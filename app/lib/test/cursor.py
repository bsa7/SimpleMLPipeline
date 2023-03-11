''' This file contains Cursor class definition for inmemory mongo test class '''

class Cursor:
  ''' This class contains emulation result of find in collection '''
  def __init__(self, results = None):
    self.__results = results or []

  def sort(self, _rules):
    ''' Sorts (not) results by given rules '''
    return Cursor(self.__results)

  def limit(self, count):
    ''' Returns first count elements '''
    return Cursor(self.__results[:count])

  def next(self):
    ''' Returns next available elements from end of results '''
    return self.__results.pop()
