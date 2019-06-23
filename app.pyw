import pyautogui
import os
from datetime import datetime


# Ruta del repositorio
path = 'data'

# Obtener la fecha
get_date = datetime.now()
date = get_date.strftime('%Y%m%d%H%M%S')


# Funcion para realizar screenshot
def get_screenshot(path, date):

    # Comprobar existencia del directorio
    if (os.path.exists(path)):
        # Capturar Pantalla
        screenshot = pyautogui.screenshot()    
        # Guardar Imagen
        screenshot.save(path + '/screenshot_' + date + '.jpg')
        
    else:
        # Crear directorio repositorio
        os.mkdir(path)
        # Capturar Pantalla
        screenshot = pyautogui.screenshot()    
        # Guardar Imagen
        screenshot.save(path + '/screenshot_' + date + '.jpg')


get_screenshot(path, date)