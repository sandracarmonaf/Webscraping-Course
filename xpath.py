import requests
from lxml import html

url = 'https://juansalinasponce.github.io/'
response = requests.get(url)
tree = html.fromstring(response.content)

nombre = tree.xpath('//h1/text()')
print(nombre[0])  # Salida: Sandra Carmona