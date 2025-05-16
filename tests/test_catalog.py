from pom.catalog_page import CatalogPage

def test_opencart_catalog_find_catalog_list(browser, base_url):
    CatalogPage(browser,base_url).catalog_list
   
def test_opencart_catalog_find_button_continue(browser, base_url):
    CatalogPage(browser,base_url).button_continue
    
def test_opencart_catalog_content_text(browser, base_url):
    CatalogPage(browser,base_url).content_text
    
def test_opencart_catalog_home(browser, base_url):
    CatalogPage(browser,base_url).home

def test_opencart_catalog_cameras(browser, base_url):
    CatalogPage(browser,base_url).cameras
   
