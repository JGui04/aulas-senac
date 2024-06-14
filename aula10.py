# importar para o projeto
# python -m pip install BeautifulSoup4
# python -m pip install requests
import requests
from bs4 import BeautifulSoup

# Coletar para analisar a primeira pagina de cotações
page = requests.get('https://valorinveste.globo.com/cotacoes/')
soup = BeautifulSoup(page.text, 'html.parser')

# Passar a classe para a variável
acao = soup.find(class_='vd-table')

# Pegar todas as instancias da tag TD dentro da Class=vd-table
acaoItems = acao.find_all('td')

print(acaoItems)


response = page.text
responseStatus = page
# Verificaremos se foi bem-sucedida a comunicação

if responseStatus.status_code == 200:
    # Cria um objeto BeautifulSoup com todo o conteúdo da página HTML
    soup = BeautifulSoup(responseStatus.content, 'html.parser')
    
    # Encontre elementos específicos na página usando os seletores do CSS
    # Vamos pegar todos os link's desta página
    links = soup.select('a')

    # Imprimir todos os seus atributos
    for link in links:
        href = link.get('href')
        text = link.get_text()
        print(f'{text}')
        print(f'URL do link {href}\n\n\n')
        
else:
    print("Falha na requisição HTTPS")