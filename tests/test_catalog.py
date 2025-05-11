from pom.catalog_page import CatalogPage

def test_opencart_catalog_find_catalog_list(browser, base_url):
    CatalogPage(browser,base_url).get_element("#column-left > div.list-group.mb-3","css")
   
def test_opencart_catalog_find_button_continue(browser, base_url):
    CatalogPage(browser,base_url).get_element("#content > div > a","css")
    
def test_opencart_catalog_content_text(browser, base_url):
    CatalogPage(browser,base_url).get_element("#content > h1","css")
    
def test_opencart_catalog_home(browser, base_url):
    CatalogPage(browser,base_url).get_element("#error-not-found > ul > li:nth-child(1) > a","css")

def test_opencart_catalog_cameras(browser, base_url):
    CatalogPage(browser,base_url).get_element("#column-left > div.list-group.mb-3 > a:nth-child(7)","css")
   
