from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pom.base_page import BasePage,OpenPageMixin
import allure

@allure.epic("Работаем со странице Смартфоны")
class SmartphonePage(BasePage,OpenPageMixin):
    @allure.step("Открываем страницу Смартфоны.")
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/en-gb/catalog/smartphone" )
        self.open_page(self.path) 

    @allure.feature("Собираем цены на странице.")   
    @allure.step("Произвожу копирование цен на странице Смартфоны.")
    def get_prices(self):
        self.logger.info("Copy prices on Main page.")
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
        )
        return [float(price.text.replace('€', '').replace('£', '').replace('$', '').strip()) 
                for price in self.browser.find_elements(By.CSS_SELECTOR, ".price-new")]
    
    @property
    def Currency_button(self):
        return {"element":WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        '#form-currency'))),"name":"Кнопка валют"}
    
    def Currency(self,id_curruncy):
        return {"element":WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        f'#form-currency > div > ul > li:nth-child({id_curruncy}) > a'))),"name":"Валюта"}