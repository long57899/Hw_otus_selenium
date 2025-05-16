from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

        
class BasePage:
    def __init__(self, browser, base_url, path=""):
        self.browser = browser
        self.base_url = base_url
        self.path = path
        
    def get_element(self, element_selector:str):
        if element_selector[0] == "/":
            return WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,element_selector)))
        else:
            return WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,element_selector)))
        
    def input_value(self, element, text: str):
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(element))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self.browser).move_to_element(element).pause(1.5).click(element).perform()
        element.clear()
        for letter in text:
            element.send_keys(letter)
        
    def click_element(self,element):
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(element))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self.browser).move_to_element(element).pause(1.5).click(element).perform()
       
    def element_alert_to_disappear(self):
        WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"#alert > div")))


class OpenPageMixin:
    def open_page(self, path=""):
        try:
            full_url = f"{self.base_url}{path}"
            self.browser.get(full_url)
            return self
        except Exception as e:
            raise Exception(f"Failed to open page {full_url}: {str(e)}")