
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
	

	            ## meter en la nueva pagina de resewrvas(horas)


	handles=driver.window_handles ## devuelve lista de todos los handles(id pagina)
	for handle in handles:
	 	driver.switch_to.window(handle)  ##me cambio a la pagina de las horas




	 			## selecciono la hora manualmente y el numero de jugadores

	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="page"]/div/div[3]/div[2]/div[2]/div[69]/div[2]/div[1]').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/table/tr[1]/td[3]/div/span[3]').click()



				##Escribo el nombre de los jugadores

	## nombre del primer jugador

	driver.find_element_by_xpath('//*[@id="page"]/div/div[3]/div/table/tr[2]/td/div[1]/input').send_keys(k["nom1"])
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[3]/div/div').click()

	## nombre del segundo jugador

	driver.find_element_by_xpath('//*[@id="page"]/div/div[3]/div/table/tr[2]/td/div[2]/input').send_keys(k["nom2"])
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[3]/div/div').click()

	## nombre del tercer jugador

	driver.find_element_by_xpath('//*[@id="page"]/div/div[3]/div/table/tr[2]/td/div[3]/input').send_keys(k["nom3"])
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[3]/div/div').click()




	







	time.sleep(10)

	




	


	driver.quit()


if __name__=='__main__':
	reservar(keys)
