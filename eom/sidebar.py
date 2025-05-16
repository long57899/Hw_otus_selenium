from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pom.base_page import BasePage,OpenPageMixin
class Catalog(BasePage,OpenPageMixin):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.catalog = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-catalog")))
        self.products = super().get_element('//*[@id="collapse-1"]/li[2]/a') 
    