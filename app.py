from fastapi import FastAPI
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware

import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # A list of origins that are allowed to make requests
    allow_credentials=True, # Whether credentials (cookies, authorization headers, etc.) are allowed
    allow_methods=["*"], # A list of HTTP methods that are allowed
    allow_headers=["*"], # A list of HTTP headers that are allowed
)

async def random():

    r = requests.get('https://hikmatlar.uz/random/quote')

    soup = BeautifulSoup(r.text, 'lxml')

    quotes = soup.find_all('div', {
      'class':'card clickable'
    })

    data = []
    for i in quotes:

      # temp data
      idata = {}

      # tags
      author = i.find('a',)

      quote = i.find('h3', {
        'class':'title both-center'
      })

      view = i.find('span', {
        'class':'view_count'
      })
      
      # fill data
      if author:
        print(author)
        idata['author'] = author['href']    
        
      if quote:
        idata['quote'] = str(quote.text).strip()

      if view:
        idata['view'] = view.text

      data.append(idata)

    return data

@app.get("/")
async def root():
  return await random()