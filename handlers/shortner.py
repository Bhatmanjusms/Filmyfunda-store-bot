import requests
from configs import Config

def short(url):
      print()
      params = {'api':Config.API_KEY,#'a85e8131ddd156a0b673a35675d01c4dbee914d9',
                'url': url}
      api_url = Config.API_URL #'https://tnshort.net/api'
      res = requests.get(api_url,params=params)
      return res.json()["shortenedUrl"]
   
