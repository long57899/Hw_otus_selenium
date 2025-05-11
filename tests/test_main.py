from pom.main_page import MainPage

def test_opencart_main_find_dekstops_dropdawn(browser,base_url):
    MainPage(browser,base_url).get_element(".nav-item.dropdown:first-child","css")

def test_opencart_main_find_cart(browser,base_url):
    MainPage(browser,base_url).get_element("#header-cart > div > button","css")
    
def test_opencart_main_find_img(browser,base_url):
    MainPage(browser,base_url).get_element('img[alt="iPhone 6"]',"css")
  
def test_opencart_main_find_button_add_to_cart(browser,base_url):
    MainPage(browser,base_url).add_button_to_cart(1)
  
def test_opencart_main_find_my_account(browser,base_url):
    MainPage(browser,base_url).get_element("body > footer > div > div > div:nth-child(4) > ul > li:nth-child(1) > a","css")
 
