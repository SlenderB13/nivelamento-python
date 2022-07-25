from bs4 import BeautifulSoup

with open('parte-5/example.html') as file:
    soup = BeautifulSoup(file)

text = soup.find('p').text
print(text)