from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

def login_workana(email, senha):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(os.getenv('URL_WORKANA'))
    time.sleep(5)
    
    try:
        cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        cookies.click()
        print("Aceitou os cookies!")
    except NoSuchElementException:
        pass
    user_input = driver.find_element(By.NAME, 'email')
    pass_input = driver.find_element(By.NAME, 'password')
    user_input.send_keys(email)
    pass_input.send_keys(senha)
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("Logou no workana!")
    time.sleep(5)
    return driver

def executar_bot(email, senha):
    driver = login_workana(email, senha)
    driver.quit()
