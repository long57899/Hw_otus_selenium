from pom.register_page import RegisterPage
import time

def test_opencart_register_input_first_name(browser, base_url):
    RegisterPage(browser, base_url).input_first_name

def test_opencart_register_input_last_name(browser, base_url):
    RegisterPage(browser, base_url).input_last_name
    

def test_opencart_register_input_email(browser, base_url):
    RegisterPage(browser, base_url).input_email   

def test_opencart_register_input_password(browser, base_url):
    RegisterPage(browser, base_url).input_password
       
def test_opencart_register_checkbox_subscribe(browser, base_url):
    RegisterPage(browser, base_url).newsletter

def test_register_new_customer(browser,base_url):
    Rp = RegisterPage(browser,base_url)
    Rp.register("test_first_name","test_last_name","test-email@gmail.com","test_password")
    time.sleep(2)
    result = Rp.get_element("#content > h1","css")
    assert "Your Account Has Been Created!" in result.text