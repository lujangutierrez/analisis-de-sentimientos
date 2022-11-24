import matplotlib.pyplot as plt

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

finviz_url = 'https://fiviz.com/quote.ashx?t='
tickers = ['AMZN', 'GOOG', 'FB']

news_tables = {}
for ticker in tickers:
    url = finviz_url + ticker
    req = Request(url=url, headers={'user-agent': 'myapp'})
    response = urlopen(req)

    html = BeautifulSoup(response, features='html.parser')
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table
    break

# amzn_data = news_table['AMZN']
# amzn_rows = amzn_data.findall('tr')
# for index, row in enumerate(amzn_rows):
#     tittle = row.a.text
#     timestamp = row.td.text
#     print(timestamp + " " + tittle)

parsed_data = []
for ticker, news_table in news_table.items():

    for row in news_table.findAll('tr'):

        title = row.a.text
        date_data = row.td.text.splet ('')
        if len(date-date_data) == 1:
            time = date_data
        else:
            date = date_data[0]
            time = date_data[1]
        parsed_data.append([ticker, date, time, title])

df = pd.DataFrame(parsed_data, columns=['ticker','date','time','title'])
vader = SentimentIntensityAnalyzer()

print(vader.polarity_scores("i dont think apple is a good company."))

f = lambda title: vader.polarity_scores(title)['compound']
df ['compound'] = df['title'].apply()
df['date'] = pd.to_datetime(df.date).dt.date

plt.figure(figsize=(10-8))

mean_df = df.groupby(['ticker','date']).mean()
mean_df = mean_df.unstack()
mean_df = mean_df.xs('compound', axis = "columns").transpose()
mean_df.plot(kind=''
print(mean_df)
