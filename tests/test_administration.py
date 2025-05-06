from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_opencart_administration_find_modal(browser, base_url):
    browser.get(f"{base_url}/administration")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#form-login'))
    )

def test_opencart_administration_find_username(browser, base_url):
    browser.get(f"{base_url}/administration")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-username'))
    )

def test_opencart_administration_find_password(browser, base_url):
    browser.get(f"{base_url}/administration")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-password'))
    )
   
def test_opencart_administration_find_button_login(browser, base_url):
    browser.get(f"{base_url}/administration")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#form-login > div.text-end > button'))
    )

def test_opencart_administration_find_footer(browser, base_url):
    browser.get(f"{base_url}/administration")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#footer'))
    )
    