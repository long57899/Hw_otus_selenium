from selenium.webdriver.common.alert import Alert

def alert(browser):
    try:
        return Alert(browser)
    except:
        print("Alert not catched!")
  