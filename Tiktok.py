import requests
from bs4 import BeautifulSoup
from config import COOKIES, PARAMS, HEADERS

def getUrl(link):
  returnFunc = {
    "status" : False,
    "message": str(),
    "data" : []
  }
  DATA = {
      'id': str(link),
      'locale': 'en',
      'tt': 'eHQyWFM2',
  }

  try:
    response = requests.post('https://ssstik.io/abc', params=PARAMS, cookies=COOKIES,       headers=HEADERS, data=DATA)
    
    responseHTML = BeautifulSoup(response.content, "html.parser")
    
    for a in responseHTML.find_all("a", href=True):
      returnFunc["data"].append({a.text.replace("\n", " ") : a['href']})
      returnFunc['status'] = True
    
    return returnFunc
 
  except Exception as e:
    returnFunc['message'] = e
    return returnFunc
    
