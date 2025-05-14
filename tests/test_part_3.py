from pom.admin_page import AdminPage
from pom.main_page import MainPage
from eom.header import Currency_button,Currency
import time


def test_opencart_scenario_1_login(browser, base_url, load_env):
    Ac = AdminPage(browser,base_url)
    Ac.login()

    assert "Dashboard" in Ac.title_admin.text
    Ac.logout()
       
def test_opencart_scenario_2_cart(browser, base_url):
    Mp = MainPage(browser, base_url)
    browser.maximize_window()

    time.sleep(2)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    add_iphone = Mp.add_button_to_cart(2)
    Mp.click_element(add_iphone)

    browser.execute_script("window.scrollTo(0, 0);")

    Mp.element_has_gone("#alert .alert alert-success alert-dismissible")
    
    cart = Mp.get_element("#top > div > div.nav.float-end > ul > li:nth-child(4)","css")

    time.sleep(6)
   
    Mp.click_element(cart)
    
    content_cart = Mp.get_element( '#shopping-cart > div > table > tbody > tr > td.text-start.text-wrap > a' , "css")
 
    assert "iPhone" in content_cart.text

def test_opencart_scenario_3_change_currency_main(browser, base_url):
    Mp = MainPage(browser,base_url)

    prices_1 = Mp.get_prices()

    currency_button_on_main = Currency_button(browser,'#form-currency')

    Mp.click_element(currency_button_on_main)

    euro = Currency(browser,1)
    
    Mp.click_element(euro)
    
    prices_2 = Mp.get_prices()

    currency_button_on_main = Currency_button(browser,'#form-currency')
    
    Mp.click_element(currency_button_on_main)

    gbp = Currency(browser,2)
    
    Mp.click_element(gbp)

    prices_3 = Mp.get_prices()

    assert prices_1 != prices_2 != prices_3

def test_opencart_scenario_4_change_currency_catalog(browser, base_url):
    
    Mp = MainPage(browser,base_url, path="/en-gb/catalog/smartphone")

    prices_1 = Mp.get_prices()

    currency_button_on_main = Currency_button(browser,'#form-currency')

    Mp.click_element(currency_button_on_main)

    euro = Currency(browser,1)
    
    Mp.click_element(euro)
    
    prices_2 = Mp.get_prices()

    currency_button_on_main = Currency_button(browser,'#form-currency')
    
    Mp.click_element(currency_button_on_main)

    usd = Currency(browser,3)
    
    Mp.click_element(usd)

    prices_3 = Mp.get_prices()

    assert prices_1 != prices_2 != prices_3
