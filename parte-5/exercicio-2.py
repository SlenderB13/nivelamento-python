from bs4 import BeautifulSoup

with open('parte-5/example.html') as file:
    soup = BeautifulSoup(file)

all_paragraphs = soup.find_all('p')
print(all_paragraphs)