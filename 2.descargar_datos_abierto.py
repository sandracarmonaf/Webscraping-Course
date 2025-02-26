from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Configuración de opciones para el navegador
download_dir = r"C:\Users\juan1\OneDrive\Documentos\webscraping\descargas"  # Cambia esto a tu ruta de descarga deseada

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)
#chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-dev-shm-usage")

# Configurar preferencias de descarga
prefs = {
    "download.default_directory": download_dir,  # Cambia la carpeta de descarga
    "download.prompt_for_download": False,  # No preguntar para descargar
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True  # Habilitar la navegación segura
}
chrome_options.add_experimental_option("prefs", prefs)

# Inicializar el navegador
serv = Service(executable_path='C:\driver\chromedriver.exe')
driver = webdriver.Chrome(service=serv,options=chrome_options)

# URL de la página donde se encuentra el archivo
url = "https://www.datosabiertos.gob.pe/dataset/consumo-energ%C3%A9tico-de-clientes-hidrandina-distriluz-dlz"

driver.get(url)

try:
    # Esperar un poco para que la página cargue
    time.sleep(5)  # Ajusta el tiempo según sea necesario

    # Encuentra el enlace de descarga y haz clic en él
    # Cambia el selector según la estructura de la página
    download_button = driver.find_element(By.XPATH, "//a[contains(@href, '_DatosAbiertos_consumohdna_281222.csv')]")
    download_button.click()
    # Esperar un poco para que la descarga se complete
    #time.sleep(10)  # Ajusta el tiempo según el tamaño del archivo
    
    # Esperar a que la descarga se complete
    file_name = "_DatosAbiertos_consumohdna_281222.csv"  # Nombre del archivo a descargar
    file_path = os.path.join(download_dir, file_name)
    
    # Esperar hasta que el archivo se descargue completamente
    while True:
        if os.path.exists(file_path):
            # Verificar si el archivo tiene la extensión temporal
            if not file_path.endswith('.crdownload'):
                break
        time.sleep(1)  # Esperar un segundo antes de volver a comprobar

    print("La descarga se completó.")
    

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Cerrar el navegador
    driver.quit()