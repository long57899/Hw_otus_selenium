from pom.admin_page import AdminMainPage
from pom.main_page import MainPage
from pom.smartphone import SmartphonePage
import time


def test_opencart_scenario_1_login(browser, base_url,get_login ):
    Amp = AdminMainPage(browser,base_url)
    Amp.login(get_login)
    assert "Dashboard" in Amp.title_admin.text
    Amp.logout()
       
def test_opencart_scenario_2_cart(browser, base_url):
    Mp = MainPage(browser, base_url)
    browser.maximize_window()
    time.sleep(2)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    add_iphone = Mp.add_button_to_cart(2)
    Mp.click_element(add_iphone)
    browser.execute_script("window.scrollTo(0, 0);")
    time.sleep(6)    
    Mp.click_element(Mp.cart)

    assert "iPhone" in Mp.content_cart.text

def test_opencart_scenario_3_change_currency_main(browser, base_url):
    Mp = MainPage(browser,base_url)

    Mp.click_element(Mp.Currency_button)
    usd = Mp.Currency(3)
    Mp.click_element(usd)
    prices_1 = Mp.get_prices()

    Mp.click_element(Mp.Currency_button)
    euro = Mp.Currency(1)
    Mp.click_element(euro)
    prices_2 = Mp.get_prices()

    Mp.click_element(Mp.Currency_button)
    gbp = Mp.Currency(2)
    Mp.click_element(gbp)
    prices_3 = Mp.get_prices()
    time.sleep(1)


    assert prices_1 != prices_2 != prices_3

def test_opencart_scenario_4_change_currency_catalog(browser, base_url):
    Sp = SmartphonePage(browser,base_url)

    Sp.click_element(Sp.Currency_button)
    gbp = Sp.Currency(2)
    Sp.click_element(gbp)
    prices_1 = Sp.get_prices()

    Sp.click_element(Sp.Currency_button)
    euro = Sp.Currency(1)
    Sp.click_element(euro)
    prices_2 = Sp.get_prices()
    
    Sp.click_element(Sp.Currency_button)
    usd = Sp.Currency(3)
    Sp.click_element(usd)
    prices_3 = Sp.get_prices()

    time.sleep(1)
    assert prices_1 != prices_2 != prices_3
