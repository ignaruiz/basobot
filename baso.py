
from config import keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def reservar(k):
	
## creo el driver para acceder a la pagina web basozabal
	
	options = Options()
	options.add_argument('--no-sandbox') 

	driver=webdriver.Chrome(options=options, executable_path='./chromedriver')

	driver.get(k['baso_url'])

## lenguaje xpath para buscar y procesar elementos html de la pagina

				##usuario y contraseña

	driver.find_element_by_xpath('//*[@id="u12"]').send_keys(k["usuario"])
	driver.find_element_by_xpath('//*[@id="c12"]').send_keys(k["contraseña"])
	driver.find_element_by_xpath('//*[@id="privada"]/section/div/div/div[2]/div/div[1]/form[1]/div[2]/a').click()


				## meter en la pagina de reservas

		
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="opcionMenu_29"]/a').click()

	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="body"]/main/section/div[2]/div[1]/a').click()
	
	time.sleep(4)
	driver.find_element_by_xpath('//*[@id="page"]/div/div[3]/div[2]/div[2]/div[57]/div[2]/div[1]').click()
	time.sleep(1)
	
	

	


	driver.quit()


if __name__=='__main__':
	reservar(keys)
