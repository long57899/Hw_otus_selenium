from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def alert(browser):
    try:
        alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
        alert_obj = Alert(browser)
        return alert_obj
    except:
        print("Alert not catched!")
  