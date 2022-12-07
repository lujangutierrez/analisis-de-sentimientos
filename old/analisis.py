import matplotlib.pyplot as plt
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

finviz_url = 'https://fiviz.com/quote.ashx?t='
tickers = ['AMZN']

news_tables = {}
for ticker in tickers:
    url = finviz_url + ticker ##toma el urlfinviz y lo completa con un ticker del array tickers

    req = Request(url=url, headers={'user-agent': 'my-app'}) ##el url=url el parametro url que es igual a la variable url. y después especificas los 'headers' nos ayuda a requerir la data, sino no nos va a dejar acceder al url de finviz
    response = urlopen(req) ## es lo que trae req
    print(response)

    