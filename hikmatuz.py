import requests
from bs4 import BeautifulSoup

class HikmatUz():

  def __init__(self) -> None:
    pass

  def random(self):

    r = requests.get('https://hikmatlar.uz/random/quote')

    soup = BeautifulSoup(r.text, 'lxml')

    quotes = soup.find_all('div', {
      'class':'card clickable'
    })

    data = []
    for i in quotes:

      author:str = i.find('a',)['href']

      quote:str = i.find('h3', {
        'class':'title both-center'
      }).text

      view:str = i.find('span', {
        'class':'view_count'
      }).text

      data.append(
        {
          "author":author.strip(),
          "quote":quote.strip(),
          "view":view.strip(),
        }
      )

    print(data)

    

HikmatUz().random()