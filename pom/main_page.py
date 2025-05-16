from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pom.base_page import OpenPageMixin,BasePage

class MainPage(BasePage,OpenPageMixin):
    def __init__(self, browser, base_url, path=""):
        super().__init__(browser, base_url, path)
        self.open_page(self.path)    
        self.form_currency = super().get_element("#form-currency")
        self.dekstops_dropdawn = super().get_element(".nav-item.dropdown:first-child")
        self.img_iphone = super().get_element('img[alt="iPhone 6"]')
        self.my_account = super().get_element("body > footer > div > div > div:nth-child(4) > ul > li:nth-child(1) > a")

    def add_button_to_cart(self,number_product_thumb):
        return super().get_element(f'//*[@id="content"]/div[2]/div[{number_product_thumb}]/div/div[2]/form/div/button[1]')
    
    @property 
    def cart(self):
        return super().get_element('#top > div > div.nav.float-end > ul > li:nth-child(4)')
    
    @property 
    def content_cart(self):
        return super().get_element('#shopping-cart > div > table > tbody > tr > td.text-start.text-wrap > a')

    @property    
    def get_prices(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
        )
        return [float(price.text.replace('€', '').replace('£', '').replace('$', '').strip()) 
                for price in self.browser.find_elements(By.CSS_SELECTOR, ".price-new")]
    
    @property
    def Currency_button(self):
        return WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#form-currency')))
   
    def Currency(self,id_curruncy):
        return WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        f'#form-currency > div > ul > li:nth-child({id_curruncy}) > a')))