from bs4 import BeautifulSoup
import requests

website = requests.get('https://www.python.org')

soup = BeautifulSoup(website.content)
links = [] 
for li in soup.find_all('li'):
    a = li.find('a', href=True)
    links.append(a.attrs['href'])

print(links)
# usar find all