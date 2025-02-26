from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Configurar opciones del navegador (opcional)
firefox_options = Options()
firefox_options.add_argument("--headless")  # Ejecutar en modo sin interfaz gráfica (opcional)

# Instalar automáticamente GeckoDriver y configurar el servicio
service = Service(GeckoDriverManager().install())

# Crear la instancia del driver
driver = webdriver.Firefox(service=service, options=firefox_options)

#Abre una página web
driver.get('https://juansalinasponce.github.io/')

# Imprime el título de la página
print(driver.title)

# Cierra el navegador
driver.quit()
