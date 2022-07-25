from bs4 import BeautifulSoup
import requests

def get_all_paragraphs(url):
    page = requests.get(url)
    print(BeautifulSoup(page.content).find_all('p'))

get_all_paragraphs('https://www.github.com/slenderb13')