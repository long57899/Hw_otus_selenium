from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_opencart_register_input_first_name(browser, base_url):
    browser.get(f"{base_url}/index.php?route=account/register")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-firstname'))
    )

def test_opencart_register_input_last_name(browser, base_url):
    browser.get(f"{base_url}/index.php?route=account/register")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-lastname'))
    )

def test_opencart_register_input_email(browser, base_url):
    browser.get(f"{base_url}/index.php?route=account/register")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-email'))
    )    

def test_opencart_register_input_password(browser, base_url):
    browser.get(f"{base_url}/index.php?route=account/register")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-password'))
    )   

def test_opencart_register_checkbox_subscribe(browser, base_url):
    browser.get(f"{base_url}/index.php?route=account/register")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-newsletter'))
    ) 