from pom.main_page import MainPage

def test_opencart_main_find_dekstops_dropdawn(browser,base_url):
    MainPage(browser,base_url).dekstops_dropdawn

def test_opencart_main_find_cart(browser,base_url):
    MainPage(browser,base_url).cart
    
def test_opencart_main_find_img(browser,base_url):
    MainPage(browser,base_url).img_iphone
  
def test_opencart_main_find_button_add_to_cart(browser,base_url):
    MainPage(browser,base_url).add_button_to_cart(1)
  
def test_opencart_main_find_my_account(browser,base_url):
    MainPage(browser,base_url).my_account
 
