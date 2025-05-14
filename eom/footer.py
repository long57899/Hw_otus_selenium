from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_footer(browser:tuple):
    try: 
        return WebDriverWait(browser,100).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#footer'))
    )
    except: 
        print(f"On page {browser} not found: footer")
        return None 