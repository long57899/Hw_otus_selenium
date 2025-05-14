from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pom.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, browser, base_url, path=""):
        super().__init__(browser, base_url, path)

    def add_button_to_cart(self,number_product_thumb):
        return super().get_element(f'//*[@id="content"]/div[2]/div[{number_product_thumb}]/div/div[2]/form/div/button[1]',"xpath")
        
    def get_prices(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
        )
        return [float(price.text.replace('€', '').replace('£', '').replace('$', '').strip()) 
                for price in self.browser.find_elements(By.CSS_SELECTOR, ".price-new")]