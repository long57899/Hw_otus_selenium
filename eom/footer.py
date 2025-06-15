from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

@allure.step("Получение футера")
def get_footer(browser:tuple):
    return {"element":WebDriverWait(browser,100).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#footer'))),"name":"Футер"}
    