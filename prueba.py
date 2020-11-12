
from config import keys
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox') 
driver=webdriver.Chrome(options=options, executable_path='./chromedriver')

driver.get('https://www.marca.com/')

driver.quit()