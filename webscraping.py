import pandas as pd
from bs4 import BeautifulSoup
import requests

url1="https://www.nasa.gov/feature/jpl/nasas-next-mars-mission-to-investigate-interior-of-red-planet"
r = requests.get(url1)
data = r.text
soup = BeautifulSoup(data, features="html.parser")

news_title = soup.title.text
print(news_title)

tags = soup.find(attrs={"name":"dc.description"})
news_p = tags.get('content')
print(news_p)


url1 = "https://space-facts.com/mars/"
page = requests.get(url1)
data = page.text
soup = BeautifulSoup(data, 'html.parser')
table = soup.find_all("table")
for mytable in table:
    table_body = mytable.find('tbody')
    rows = table_body.find_all('tr')
    for tr in rows:
        print ("<tr>")
        cols = tr.find_all('td')
        for td in cols:
            print ("<td>",td.text, "</td>")
        print ("</tr>")
#df = pd.read_html(str(table))


