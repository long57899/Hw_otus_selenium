from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_opencart_catalog_find_catalog_list(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    "#column-left > div.list-group.mb-3"))
    )

def test_opencart_catalog_find_button_continue(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    "#content > div > a"))
    )

def test_opencart_catalog_content_text(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    "#content > h1"))
    )

def test_opencart_catalog_home(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    "#error-not-found > ul > li:nth-child(1) > a"))
    )

def test_opencart_catalog_cameras(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    "#column-left > div.list-group.mb-3 > a:nth-child(7)"))
    )
