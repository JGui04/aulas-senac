# importar para o projeto
# python -m pip install BeautifulSoup4
# python -m pip install requests
import requests
from bs4 import BeautifulSoup

#coletar e analisar a primeira pagina
soup = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

soup2 = BeautifulSoup(soup.text,'html.parser')

# pegar todo o texto da div BodyText
name_list = soup2.find(class_='BodyText')

# pegar o texto de todas as instacias da tag <a> dentro da div BodyText
name_list_items = name_list.find_all('a')

print(name_list_items)