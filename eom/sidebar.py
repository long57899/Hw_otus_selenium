from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def element_catalog(browser,timeout=10):
    try:
        catalog = WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-catalog")))
        return catalog
    except:
        print("Not found catalog in this page!")