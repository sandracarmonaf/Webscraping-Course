import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Configuración de opciones para el navegador
#chrome_options = Options()
#chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)
##chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-dev-shm-usage")

URL = "https://checatuslineas.osiptel.gob.pe/"
DRIVER_LOCATION = "C:\driver\chromedriver.exe"
TIPO_DOCUMENTO = "01"  # TIPO DNI
NUMERO_DOCUMENTO = "71752727" # NUMERO DE DNI

def initializing_driver_and_wait(driver_path):
    serv = service.Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    #driver = webdriver.Chrome(service=serv, options=options)
    driver = webdriver.Chrome(service=serv)
    driver.delete_all_cookies()
    driver.maximize_window()
    return driver, WebDriverWait(driver, 3)
    # return driver

if __name__ == '__main__':
    chrome_driver, chrome_wait_driver = initializing_driver_and_wait(DRIVER_LOCATION)
    chrome_driver.get(URL)
    select_element = chrome_wait_driver.until(EC.presence_of_element_located((By.ID, "IdTipoDoc")))
    select = Select(select_element)
    select.select_by_value("1")

    # Si necesitas esperar para ver el resultado
    time.sleep(3)

    input_element = chrome_wait_driver.until(EC.presence_of_element_located((By.ID, "NumeroDocumento")))
    # Limpiar el campo (opcional, si ya tiene texto)
    input_element.clear()

    # Enviar valor-
    input_element.send_keys(NUMERO_DOCUMENTO)

    time.sleep(3)

    button_element = chrome_wait_driver.until(EC.presence_of_element_located((By.ID, "btnBuscar")))
    button_element.click()

    time.sleep(3)

    table_element = chrome_wait_driver.until(EC.presence_of_element_located((By.ID, "GridConsulta")))
    try:
        # rows = table_element.find_elements(By.CSS_SELECTOR, "tbody tr[role='row']")
        rows = chrome_wait_driver.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr[role='row']")))
        for row in rows:
            # Encontrar todas las etiquetas <td> con la clase "text-center align-middle" dentro de la fila
            row_values = row.find_elements(By.CLASS_NAME, "text-center.align-middle")

            # Obtener los valores de las etiquetas <td> e imprimirlos
            data = [value.text for value in row_values]
            print(data)
    except selenium.common.exceptions.TimeoutException as e: 
        print("No se encontraron valores de respuesta del DNI: ", e)