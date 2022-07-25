from bs4 import BeautifulSoup
import requests

def search_by_id(url, id):
    page = requests.get(url)
    print(BeautifulSoup(page.content).find_all(id=id))

search_by_id('https://www.python.org', 'top')