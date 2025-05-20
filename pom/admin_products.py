from pom.base_page import BasePage,OpenPageMixin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import allure

@allure.epic("Страница Продуктов в Админке.")
class AdminProductsPage(BasePage,OpenPageMixin):
    def __init__(self, browser,base_url):
        super().__init__(browser,base_url)
        self.add_button_on_products = super().get_element('#content > div.page-header > div > div > a', "Кнопка добавить продукт.")
    
    @allure.feature("Добавление продукта")
    @allure.step("Добавляю новый продукт через страницу админа.")    
    def add_new_product(self,product_data):
        '''Функция создания нового продукта через страницу администратора.'''
        self.logger.info("Start to add new product on Opencart.")
        try:
            self.logger.info(f"Start to input {product_data} on Admin page.")
            input_name_product = super().get_element('#input-name-1',"Название продукта")
            input_meta_product = super().get_element('#input-meta-title-1',"Мета продукта")
            tab_data_product = super().get_element('#form-product > ul > li:nth-child(2) > a',"Таб Данные продукта")
            super().input_value(input_name_product,product_data.get("name"))
            super().input_value(input_meta_product,product_data.get("meta"))
            super().click_element(tab_data_product)
            time.sleep(1)
            input_model = super().get_element('#input-model',"Поле модель продукта")
            super().input_value(input_model,product_data.get("model"))
            tab_ceo = super().get_element('#form-product > ul > li:nth-child(11) > a',"Таб CEO продукта")
            super().click_element(tab_ceo)
            input_ceo = super().get_element('#input-keyword-0-1',"Поле CEO продукта")
            super().input_value(input_ceo,product_data.get("ceo"))
            self.logger.info(f"End to input {product_data} on Admin page.")
            save_button = super().get_element('#content > div.page-header > div > div > button',"Кнопка добавить продукт")
            super().click_element(save_button)
            self.logger.info("Product added on Opencart.")

        except Exception as e:
            error_msg ="Ошибка процесса создания нового продукта."
            self.logger.error(error_msg, exc_info=True)
            allure.attach(
            self.browser.get_screenshot_as_png(),
            name="error_add_product",
            attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error_msg) from e       
        
    @property
    def alert(self):
        return super().get_element("#alert > div","Модалка предупреждения")
########
    @allure.feature("Фильтр по продукту.")    
    @allure.step("Произвожу поиск {name_product} с помощью фильтра страницы админ.")
    def filter_product(self,name_product):
        '''Фильтер функция в админ странице.'''
        self.logger.info(f"Start to search {name_product} on Admin page.")

        input_filter =super().get_element("#input-name")
        super().input_value(input_filter,name_product.get("name"))
        button_filter = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-filter")))
        super().click_element(button_filter)
        self.logger.info(f"End to search {name_product} on Admin page.")

    @allure.step("Выбираю все продукты в окне результатов поиска Админ страницы.")
    @property
    def select_all_on_filter(self):
        self.logger.info("Push to button select all product on Admin page.")
        select_all = super().get_element("//*[@id='form-product']//input[1]")
        super().click_element(select_all)
    
    @allure.step("Нажимаю кнопку удалить.")
    @property
    def delete_products(self):
        self.logger.info("Push to button delete product on Admin page.")
        button_delete = super().get_element("#content > div.page-header > div > div > button.btn.btn-danger")
        super().click_element(button_delete)
    
    @property
    def alert_check(self):
        return WebDriverWait(self.browser, 10).until(EC.alert_is_present())
    
    @property
    def form_filter(self):
        return super().get_element("#form-product > div.table-responsive > table > tbody > tr > td")
