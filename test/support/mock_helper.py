''' This file contain helpers for mock external service responses '''

def stub_get_request(rsps, api_uri: str, response: dict):
  ''' This method creates a stub for a specific api endpoint and emulates a
      successful data fetch '''
  rsps.get(api_uri, json = response, status = 200)
