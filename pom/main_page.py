from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pom.base_page import OpenPageMixin,BasePage
import allure

@allure.epic("Работаем с главной страницей Опенкарт.")
class MainPage(BasePage,OpenPageMixin):
    @allure.step("Открываем главную страницу.")
    def __init__(self, browser, base_url, path=""):
        super().__init__(browser, base_url, path)
        try:
            self.logger.info("Open main page Opencart")
            self.open_page(self.path)    
            self.form_currency = super().get_element("#form-currency", "Перекллючение валют")
            self.dekstops_dropdawn = super().get_element(".nav-item.dropdown:first-child", "Дропдаун")
            self.img_iphone = super().get_element('img[alt="iPhone 6"]', "Изображение Iphone")
            self.my_account = super().get_element("body > footer > div > div > div:nth-child(4) > ul > li:nth-child(1) > a", "Кнопка Мой аккаунт")
        except Exception as e:
            error_msg ="Error open Main page."
            self.logger.error(error_msg, exc_info=True)
            allure.attach(
            self.browser.get_screenshot_as_png(),
            name="error_Main_page",
            attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error_msg) from e 

    @allure.step("Поиск кнопки Добавить в корзину.")
    def add_button_to_cart(self,number_product_thumb):
        return super().get_element(f'//*[@id="content"]/div[2]/div[{number_product_thumb}]/div/div[2]/form/div/button[1]', "Кнопка добавить")
        
    @property 
    def cart(self):
        return super().get_element('#top > div > div.nav.float-end > ul > li:nth-child(4)',"Корзина")
    
    @property 
    def content_cart(self):
        content = super().get_element('#shopping-cart > div > table > tbody > tr > td.text-start.text-wrap > a',"Содеримое корзины")
        return content.get("element")
    
    @allure.step("Произвожу копирование цен на главной странице.")
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