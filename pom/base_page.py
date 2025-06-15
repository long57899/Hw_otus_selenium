from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import logging
import allure
        
class BasePage:
    def __init__(self, browser, base_url, path=""):
        self.browser = browser
        self.base_url = base_url
        self.path = path
        self.__config_logger()


    def __config_logger(self, to_file=False):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(self.browser.log_level)
        
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(console_handler)
        
        if to_file:
            log_file = f"logs/{self.browser.test_name}.log"
            os.makedirs("logs", exist_ok=True)
            
            try:
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(logging.Formatter(
                    '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
                ))
                self.logger.addHandler(file_handler)
                self.logger.info(f"Инициализирован логгер для файла {log_file}")
            except Exception as e:
                self.logger.error(f"Ошибка создания файла лога: {str(e)}")
  
    @allure.step("Произвожу поиск '{element_name}' на странице.")
    def get_element(self, element_selector:str, element_name=None) -> dict:
        '''Функция поиска и получения конкретного элемента по селектору.'''
        name = element_name or element_selector
        self.logger.info(f"Поиск элемента: {name} (Cелектор: {element_selector})")
        try:
            if element_selector.startswith("/"):
                element =  WebDriverWait(self.browser,10).until(
                    EC.presence_of_element_located((By.XPATH, element_selector)))
            else:
                element =  WebDriverWait(self.browser,10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
            self.logger.info(f"Элемент {name} успешно найден")
            
            return {"element":element,"name":name}
        
        except Exception as e:
            self.logger.error(f"Элемент {name} не найден", exc_info=True)
            allure.attach(
            self.browser.get_screenshot_as_png(),
            name=f"{name}_not_found",
            attachment_type=allure.attachment_type.PNG
        )
    
    @allure.step('Ввожу {text} в input поле.')    
    def input_value(self, element_dict: dict, text: str):
        '''Функция по буквенного ввода текста в поле инпута.'''
        if not isinstance(element_dict, dict):
            self.logger.debug("check element_dict is dict.")
           
            raise TypeError(f"Expected dict, got {type(element_dict)}")
        
        name = element_dict.get("name")
        element = element_dict.get("element")
        
        try:
            self.logger.info(f"Wait load {element} on page.")
            self.logger.info(f"Scroll to {element}")
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            self.logger.info(f"Input '{text}' in {element}.")
            ActionChains(self.browser).move_to_element(element).pause(1.5).click().perform()
            element.clear()
            for letter in text:
                element.send_keys(letter)

        except Exception as e:
            self.logger.error(f"Ошибка ввода {text} в {name}", exc_info=True)
            allure.attach(
            self.browser.get_screenshot_as_png(),
            name=f"{name}_can't write",
            attachment_type=allure.attachment_type.PNG
        )
            

    @allure.step('Нажимаю на элемент.')    
    def click_element(self,element_dict):
        '''Функция клика по элементу.'''
        name = element_dict["name"]
        try:
            self.logger.info(f"Wait for element {element_dict["element"]}")
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(element_dict["element"]))
            self.logger.info(f"Scroll to {element_dict["element"]}")
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            self.logger.info(f"Click {element_dict["element"]}")
            ActionChains(self.browser).move_to_element(element).pause(1.5).click(element).perform()

        except Exception as e:
            error_msg = f"Ошибка работы с элементом {name}. Элемент: {element_dict["element"]}"
            self.logger.error(error_msg, exc_info=True)
            allure.attach(
            self.browser.page_source,
            name=f"{name}_error_click",
            attachment_type=allure.attachment_type.HTML)
            raise AssertionError(error_msg) from e

    @allure.step("Проверяю что исчезло предупреждение.")   
    def element_alert_to_disappear(self):
        self.logger.info("Wait of desappear alert.")
        WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"#alert > div")))


class OpenPageMixin:
    def __init__(self):
        self.__config_logger()

    def __config_logger(self, to_file=False):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step("Открываю страницу.")
    def open_page(self, path=""):
        '''Функция открытия страницы.'''
        try:
            full_url = f"{self.base_url}{path}"
            self.logger.info(f"Open {full_url}")
            self.browser.get(full_url)
            return self
        except Exception as e:
            self.logger.error(f"Problem with open_page -> {e}")
            raise Exception(f"Failed to open page {full_url}: {str(e)}")