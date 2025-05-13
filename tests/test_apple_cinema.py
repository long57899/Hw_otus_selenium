from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_opencart_apple_cinema_find_add_to_wish_list(browser, base_url):
    browser.get(f"{base_url}/en-gb/product/desktops/apple-cinema")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.XPATH, 
    '//*[@id="content"]/div[1]/div[2]/form/div/button[1]/i'))
    )

def test_opencart_apple_cinema_find_select_color(browser, base_url):
    browser.get(f"{base_url}/en-gb/product/desktops/apple-cinema")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.XPATH, 
    '//*[@id="input-option-217"]'))
    )

def test_opencart_apple_cinema_find_button_cart(browser, base_url):
    browser.get(f"{base_url}/en-gb/product/desktops/apple-cinema")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.XPATH, 
    '//*[@id="button-cart"]'))
    )

def test_opencart_apple_cinema_find_tab_description(browser, base_url):
    browser.get(f"{base_url}/en-gb/product/desktops/apple-cinema")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.XPATH, 
    '//*[@id="tab-description"]'))
    )

def test_opencart_apple_cinema_find_tab_review(browser, base_url):
    browser.get(f"{base_url}/en-gb/product/desktops/apple-cinema")
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.XPATH, 
    '//*[@id="content"]/div[1]/ul/li[3]/a'))
    )