from config import keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


## funcion que nos reserva hora de salida en basozabal

def reservar(k):

    options = Options()
	options.add_argument('--no-sandbox') 

    ## creo un driver para acceder al login de la pagina

    driver=webdriver.Chrome(options=options, executable_path='./chromedriver')
    driver.get(k['url_baso'])
    
