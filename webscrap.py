import requests
import time
from bs4 import BeautifulSoup

#Getting data from the webpage Google Scholar
url = 'https://scholar.google.es/citations?user=-B2gAMEAAAAJ&hl=pt-BR'
response = requests.get(url)
#Load data ino bs4
soup = BeautifulSoup(response.text, 'html.parser')

#get data within specific element
articles = soup.find('table', {'id': 'gsc_a_t'})
tbody = articles.find('tbody')
data = []

for tr in tbody.find_all('tr'):
    titles = tr.find_all('td')[0].find_all('a')[0].text.strip()
    authors = tr.find_all('td')[0].find_all('div', {'class': 'gs_gray'})[0].text.strip()
    data.append(titles)
    #time.sleep(1)  Use this line avoid getting flagged as a spammer.
print(data)

'''
Other examples

#Getting the data by looking into each tr
data = []
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    data.append(values)
#print(data)   

#Get only the where rows are marked "gsc_a_at"
data = []
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td', {'class': 'gsc_a_t'})]
    data.append(values)
#print(data)

'''

