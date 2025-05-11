from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self,browser, base_url, path=""):
        self.browser=browser
        self.base_url = base_url
        try:
            self.browser.get(f"{self.base_url}{path}")
            self.wait = WebDriverWait(self.browser, 10)
        except Exception as e:
            raise Exception(f"Failed to open page {self.base_url}{path}: {str(e)}")
        
    def get_element(self,element_selector:str,type_selector:str):
        type_selector.lower()
        if type_selector == "css":
            try:
                return WebDriverWait(self.browser,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,element_selector))
                )
            except:
                print(f"Element not found: {element_selector}")
                return None
        
        elif type_selector == "xpath":
            try:
                return WebDriverWait(self.browser,10).until(
                EC.presence_of_element_located((By.XPATH,element_selector))
                )
            except:
                print(f"Element not found: {element_selector}")
                return None 
        else:
            print(f"Selector type not found: {type_selector}")
            return None
    
        
    def input_value(self, element, text: str):
        try:
            element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(element))
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            ActionChains(self.browser).move_to_element(element).pause(1.5).click(element).perform()
            element.clear()
            for l in text:
                element.send_keys(l)
        except:
            print(f"Element not found: {element}")
            return None
        
    def click_element(self,element):
        try:
            element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(element))
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            ActionChains(self.browser).move_to_element(element).pause(1.5).click(element).perform()
        except:
            print(f"Element not found: {element}")
            return None

    def element_has_gone(self, element, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,element)))