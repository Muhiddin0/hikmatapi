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

    return data

@app.get("/")
async def root():
  return await random()