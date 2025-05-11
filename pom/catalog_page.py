from pom.base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/en-gb/catalog")