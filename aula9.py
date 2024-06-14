# Instalar caso não enha o BeautifulSoup4 e requests
# importar para o projeto
# python -m pip install BeautifulSoup4
# python -m pip install requests
import requests
from bs4 import BeautifulSoup

url = 'https://www.vgmusic.com/music/console/nintendo/nes/'

# Variável para o parâmetro da url
htmlText = requests.get(url).text

soup = BeautifulSoup(htmlText, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
