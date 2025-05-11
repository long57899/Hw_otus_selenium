from pom.apple_cinema_page import AppleCinemaPage as ACP

def test_opencart_apple_cinema_find_add_to_wish_list(browser, base_url):
    ACP(browser,base_url).get_element('//*[@id="content"]/div[1]/div[2]/form/div/button[1]/i',"xpath")
    
def test_opencart_apple_cinema_find_select_color(browser, base_url):
    ACP(browser,base_url).get_element('//*[@id="input-option-217"]',"xpath")

def test_opencart_apple_cinema_find_button_cart(browser, base_url):
    ACP(browser,base_url).get_element('//*[@id="button-cart"]',"xpath")

def test_opencart_apple_cinema_find_tab_description(browser, base_url):
    ACP(browser,base_url).get_element('//*[@id="tab-description"]',"xpath")
    
def test_opencart_apple_cinema_find_tab_review(browser, base_url):
    ACP(browser,base_url).get_element('//*[@id="content"]/div[1]/ul/li[3]/a',"xpath")
    