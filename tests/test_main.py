from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_opencart_main_find_dekstops_dropdawn(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    ".nav-item.dropdown:first-child"))
    )
    
def test_opencart_main_find_cart(browser,base_url):
    browser.get(base_url)
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#header-cart > div > button"))
    )

def test_opencart_main_find_img(browser,base_url):
    browser.get(base_url)
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#carousel-banner-0 > div.carousel-inner > div:nth-child(1) > div > div > a > img"))
    )

def test_opencart_main_find_button_add_to_cart(browser,base_url):
    browser.get(base_url)
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1) > i"))
    )

def test_opencart_main_find_my_account(browser,base_url):
    browser.get(base_url)
    WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"body > footer > div > div > div:nth-child(4) > ul > li:nth-child(1) > a"))
    )
