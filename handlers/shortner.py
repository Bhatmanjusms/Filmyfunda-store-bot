import requests

async def short(url):
      params = {'api':'a85e8131ddd156a0b673a35675d01c4dbee914d9', 'url': url}
      api_url = 'https://tnshort.net/api'
      res = requests.get(api_url,params=params)
      return res.json()["shortenedUrl"]
   
