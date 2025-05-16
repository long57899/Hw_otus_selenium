from pom.apple_cinema_page import AppleCinemaPage as ACP

def test_opencart_apple_cinema_find_add_to_wish_list(browser, base_url):
    ACP(browser,base_url).add_to_wish_list
    
def test_opencart_apple_cinema_find_select_color(browser, base_url):
    ACP(browser,base_url).select_color

def test_opencart_apple_cinema_find_button_cart(browser, base_url):
    ACP(browser,base_url).button_cart

def test_opencart_apple_cinema_find_tab_description(browser, base_url):
    ACP(browser,base_url).tab_description
    
def test_opencart_apple_cinema_find_tab_review(browser, base_url):
    ACP(browser,base_url).tab_review
    