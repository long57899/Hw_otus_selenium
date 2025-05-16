from pom.admin_page import AdminMainPage
from pom.admin_products import AdminProductsPage
from eom.sidebar import Catalog
from eom.footer import get_footer
import time

def test_opencart_administration_find_modal(browser, base_url):
    AdminMainPage(browser,base_url).admin_modal
   
def test_opencart_administration_find_username(browser, base_url):
    AdminMainPage(browser,base_url).input_login 
   
def test_opencart_administration_find_password(browser, base_url):
    AdminMainPage(browser,base_url).input_password
    
def test_opencart_administration_find_button_login(browser, base_url):
    AdminMainPage(browser,base_url).button_login
    
def test_opencart_administration_find_footer(browser):
    get_footer(browser)
    
def test_add_new_product_admin(browser,base_url,product_data,get_login):
    Ap = AdminMainPage(browser,base_url)
    browser.maximize_window()
    Ap.login(get_login)

    Ca = Catalog(browser,base_url)
    catalog = Ca.catalog
    Ap.click_element(catalog)

    products = Ca.products
    Ap.click_element(products)

    Aprodp = AdminProductsPage(browser,base_url)
    add_button = Aprodp.add_button_on_products
    Aprodp.click_element(add_button)
    
    Aprodp.add_new_product(product_data)

    assert Aprodp.alert

def test_delete_new_product_admin(browser,base_url,product_data,get_login):
    Ap = AdminMainPage(browser,base_url)
    browser.maximize_window()
    Ap.login(get_login)
    
    Ca = Catalog(browser,base_url)
    catalog = Ca.catalog
    Ap.click_element(catalog)

    products = Ca.products
    Ap.click_element(products)

    Aprodp = AdminProductsPage(browser,base_url)
    Aprodp.filter_product(product_data)

    time.sleep(1)

    Aprodp.select_all_on_filter
    Aprodp.delete_products
    Aprodp.alert_check.accept()
    
    Aprodp.filter_product(product_data)
    time.sleep(1)
    
    assert "No results!" in Aprodp.form_filter.text
    


