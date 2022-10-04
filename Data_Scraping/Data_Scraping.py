import requests
import pandas as pd
from bs4 import BeautifulSoup


# load the page into soup:
url = "https://www.theglobeandmail.com/investing/markets/funds/CHO204.CF/"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

# find correct table:
tbl = soup.select_one(".totalreturns")

soup

# remove the first row (it's not header):
#tbl.tr.extract()

# convert the html to pandas DF:
df = pd.read_html(str(tbl))[0]

# move the first row to header:
df.columns = map(str, df.loc[0])
df = df.loc[1:].reset_index(drop=True).rename(columns={"nan": "Name"})

print(df)
