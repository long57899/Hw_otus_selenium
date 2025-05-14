from pom.admin_page import AdminPage
from eom.alert import alert
from eom.sidebar import element_catalog
from eom.footer import get_footer
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_opencart_administration_find_modal(browser, base_url):
    AdminPage(browser,base_url).admin_modal
 
def test_opencart_administration_find_username(browser, base_url):
    AdminPage(browser,base_url).input_login 
   
def test_opencart_administration_find_password(browser, base_url):
    AdminPage(browser,base_url).input_password
    
def test_opencart_administration_find_button_login(browser, base_url):
    AdminPage(browser,base_url).button_login
    
def test_opencart_administration_find_footer(browser, base_url):
    get_footer(browser)
    
def test_add_new_product_admin(browser,base_url):
    Ap = AdminPage(browser,base_url)
    browser.maximize_window()
    Ap.login()
    
    catalog = element_catalog(browser)

    Ap.click_element(catalog)

    products = Ap.get_element('//*[@id="collapse-1"]/li[2]/a',"xpath")
    Ap.click_element(products)

    add_button = Ap.get_element('#content > div.page-header > div > div > a',"css")
    Ap.click_element(add_button)

    input_name = Ap.get_element('#input-name-1', "css")
    Ap.input_value(input_name,"test_product")

    input_meta = Ap.get_element('#input-meta-title-1', "css")
    Ap.input_value(input_meta,"test_meta")

    data = Ap.get_element('#form-product > ul > li:nth-child(2) > a',"css")
    Ap.click_element(data)

    time.sleep(1)

    input_model = Ap.get_element('#input-model', "css")
    Ap.input_value(input_model,"test_model")

    ceo = Ap.get_element('#form-product > ul > li:nth-child(11) > a',"css")
    Ap.click_element(ceo)
    
    input_ceo = Ap.get_element('#input-keyword-0-1', "css")
    Ap.input_value(input_ceo,"123")

    save_button = Ap.get_element('#content > div.page-header > div > div > button',"css")
    Ap.click_element(save_button)

    assert Ap.get_element("#alert > div","css")

def test_delete_new_product_admin(browser,base_url):
    Ap = AdminPage(browser,base_url)
    browser.maximize_window()
    Ap.login()
    
    catalog = element_catalog(browser)

    Ap.click_element(catalog)

    products = Ap.get_element('//*[@id="collapse-1"]/li[2]/a',"xpath")
    Ap.click_element(products)

    input_filter =Ap.get_element("#input-name","css")
    Ap.input_value(input_filter,"test_product")

    button_filter = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-filter")))

    Ap.click_element(button_filter)

    time.sleep(1)

    select_all = Ap.get_element("//*[@id='form-product']//input[1]", 'xpath')
    Ap.click_element(select_all)
    
    button_delete = Ap.get_element("#content > div.page-header > div > div > button.btn.btn-danger", "css")
    
    Ap.click_element(button_delete)
    alert(browser).accept()
    
    Ap.input_value(input_filter,"test_product")
    Ap.click_element(button_filter)
    
    time.sleep(1)
    result = Ap.get_element("#form-product > div.table-responsive > table > tbody > tr > td","css")
    

    assert "No results!" in result.text
    
