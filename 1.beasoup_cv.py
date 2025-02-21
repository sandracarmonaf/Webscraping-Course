import requests
from bs4 import BeautifulSoup

url = "https://juansalinasponce.github.io/"

response =requests.get(url)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
    title = soup.title
    body = soup.body
    h2_all = soup.find_all('h2')
    div_all = soup.find_all('div')
    firs_div = soup.find('div')
    div_section = soup.find_all('div',class_='section')
    link = soup.find('a')
    link.get('href')

    text = soup.find('p').get_text()

    html = str(soup)

    html_bonito = soup.prettify()