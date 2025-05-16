from pom.base_page import BasePage,OpenPageMixin

class CatalogPage(BasePage,OpenPageMixin):
   def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/en-gb/catalog")
        self.open_page(self.path)    
        self.catalog_list = super().get_element("#column-left > div.list-group.mb-3")
        self.button_continue = super().get_element("#content > div > a")
        self.content_text = super().get_element("#content > h1")
        self.home = super().get_element("#error-not-found > ul > li:nth-child(1) > a")
        self.cameras = super().get_element("#column-left > div.list-group.mb-3 > a:nth-child(7)")
 