#IMPORTAR TODAS LAS LIBRERIAS Y COMPLEMENTOS DE SELENIU
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#FUNCION A EJECTUAR AUTOMATICAMENTE
def intentar_login(usuario, contrasena, driver):
    try:
        driver.get('https://relatos-de-papel-gilt.vercel.app/login')
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
        search_box.clear()
        search_box.send_keys(usuario)
        search_box = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        search_box.clear()
        search_box.send_keys(contrasena)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'indice')))  
            return True
        except:
            return False

    except Exception as e:
        return False

# LISTA DE CREDENCIALES A PROBAR 
credenciales = [
    ('ADMIN', 'ADMIN'),
    ('prueba2@sadas.com', 'OTRA_CONTRASENA'),
    ('admin@example.com', 'contraseña3'),
    ('admin@example.com', '123')
]


options = Options()
options.headless = False
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
for usuario, contrasena in credenciales:
    print(f'Intento con el usuario {usuario}')
    if intentar_login(usuario, contrasena, driver):
        print(f'Ingreso exitoso con {usuario}')
        break
    else:
        print(f'Error en el ingreso con {usuario}')
    
