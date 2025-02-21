import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


url='https://cuantoestaeldolar.pe/'

fecha_hora_actual = datetime.now()
fecha_hora_formateada = fecha_hora_actual.strftime('%Y-%m-%d %H:%M')
fecha_file= fecha_hora_actual.strftime('%Y-%m-%d')

response = requests.get(url)

companies = []
compra = []
venta = []
fecha_extraccion = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
    empresas_all = soup.find_all('div',class_='ExchangeHouseItem_item_col__gudqq')

    for empresa in empresas_all:

        #Obtenemos el valor de compra
        div_buy = empresa.find('div',class_='ValueCurrency_content_buy__Z9pSf')
        buy = div_buy.find('p').get_text()
        compra.append(buy)

        #Obtenemos el valor de venta
        div_sale = empresa.find('div',class_='ValueCurrency_content_sale__fdX_P')
        sale = div_sale.find('p').get_text()
        venta.append(sale)

        #Obtenemos el nombre de la empresa
        img = empresa.find('img')
        company = img['alt']
        companies.append(company)
        fecha_extraccion.append(fecha_hora_formateada)
    

    df = pd.DataFrame({
            'empresa': companies,
            'compra': compra,
            'venta':venta,
            'fecha_extraccion':fecha_extraccion
    })
    file = f'tipo_de_cambio_{fecha_file}.csv'
    df.to_csv(file,index=False)

    #upload_to_cloud(file)

    print("Datos guardadados correctamente")
else:
    print("Error al acceder a la pagina", response.status_code)

#function upload_to_cloud(file):
    #pasos para cargar un archivo csv a cloud.