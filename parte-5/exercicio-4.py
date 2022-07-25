from bs4 import BeautifulSoup
import requests

def print_first_paragraph(url):
    page = requests.get(url)
    print(BeautifulSoup(page.content).find('p'))

print_first_paragraph('https://www.github.com/slenderb13')