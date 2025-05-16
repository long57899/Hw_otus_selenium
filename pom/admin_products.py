from pom.base_page import BasePage,OpenPageMixin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class AdminProductsPage(BasePage,OpenPageMixin):
    def __init__(self, browser,base_url):
        super().__init__(browser,base_url)
        self.add_button_on_products = super().get_element('#content > div.page-header > div > div > a')
        
    def add_new_product(self,product_data):
        input_name_product = super().get_element('#input-name-1')
        input_meta_product = super().get_element('#input-meta-title-1')
        tab_data_product = super().get_element('#form-product > ul > li:nth-child(2) > a')
        super().input_value(input_name_product,product_data.get("name"))
        super().input_value(input_meta_product,product_data.get("meta"))
        super().click_element(tab_data_product)
        time.sleep(1)
        input_model = super().get_element('#input-model')
        super().input_value(input_model,product_data.get("model"))
        tab_ceo = super().get_element('#form-product > ul > li:nth-child(11) > a')
        super().click_element(tab_ceo)
        input_ceo = super().get_element('#input-keyword-0-1')
        super().input_value(input_ceo,product_data.get("ceo"))
        save_button = super().get_element('#content > div.page-header > div > div > button')
        super().click_element(save_button)       
        
    @property
    def alert(self):
        return super().get_element("#alert > div")
        
    def filter_product(self,name_product):
        input_filter =super().get_element("#input-name")
        super().input_value(input_filter,name_product.get("name"))
        button_filter = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-filter")))
        super().click_element(button_filter)

    @property
    def select_all_on_filter(self):
        select_all = super().get_element("//*[@id='form-product']//input[1]")
        super().click_element(select_all)
    
    @property
    def delete_products(self):
        button_delete = super().get_element("#content > div.page-header > div > div > button.btn.btn-danger")
        super().click_element(button_delete)
    
    @property
    def alert_check(self):
        return WebDriverWait(self.browser, 10).until(EC.alert_is_present())
    
    @property
    def form_filter(self):
        return super().get_element("#form-product > div.table-responsive > table > tbody > tr > td")
