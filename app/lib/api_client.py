''' This file contains class for fetch data from abstract API '''

import requests

class ApiClient:
  ''' This class is wrapper for API classes '''
  def __init__(self, api_url: str):
    self.__api_url = api_url

  def get(self, api_path: str, request_attributes: dict) -> dict:
    ''' This method implement GET request to API '''
    query: str = self.__query_string(request_attributes)
    uri: str = f'{self.__api_url}{api_path}?{query}'
    print(f'{uri=}')
    response = requests.get(uri, timeout = 1)
    return response.json()

  def __query_string(self, attributes: dict) -> str:
    ''' Builds a query string for GET request '''
    query: list[str] = []
    for key in sorted(attributes.keys()):
      query.append(f'{key}={attributes[key]}')

    return '&'.join(query)
