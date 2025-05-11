from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def Currency_button(browser,element,timeout=10):
    try: 
        return WebDriverWait(browser,timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    element))
    )
    except: 
        print(f"On page {browser} not found: {element}")
        return None 

def Currency(browser,id_curruncy,timeout=10):
    try:
        return WebDriverWait(browser,timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 
        f'#form-currency > div > ul > li:nth-child({id_curruncy}) > a'))
        )
    except:
        print(f"On page {browser} not found: {id_curruncy}")
        return None 