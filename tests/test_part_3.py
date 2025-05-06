from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_opencart_scenario_1_login(browser, base_url, load_env):
    browser.get(f"{base_url}/administration/")

    input_login = WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-username'))
    )

    input_password = WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#input-password'))
    )

    button_login = WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#form-login > div.text-end > button'))
    )

    input_login.send_keys(load_env.get("login"))
    input_password.send_keys(load_env.get("password"))
    button_login.click()

    title_admin = WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#content > div.page-header > div > h1'))
    )
    assert title_admin.text in browser.title

    button_logout = WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#nav-logout'))
    )    
    button_logout.click()


def test_opencart_scenario_2_cart(browser, base_url):
    browser.get(f"{base_url}")

    name_iphone = WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > div > h4 > a'))
    )
     
    iphone = name_iphone.text
    
    button_add_to_cart_iphone = WebDriverWait(browser,3).until(
        EC.element_to_be_clickable((By.XPATH, 
    '//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div/button[1]'))
    )
    
    ActionChains(browser).move_to_element(button_add_to_cart_iphone).pause(0.5).click().perform()

    browser.get(f"{base_url}/en-gb?route=checkout/cart")

    content_cart = WebDriverWait(browser,3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#shopping-cart > div > table > tbody > tr > td.text-start.text-wrap > a'))
    )

    assert iphone == content_cart.text

def test_opencart_scenario_3_change_currency_main(browser, base_url):
    browser.get(f"{base_url}")

    def get_prices():
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
        )
        return [float(price.text.replace('€', '').replace('£', '').replace('$', '').strip()) 
                for price in browser.find_elements(By.CSS_SELECTOR, ".price-new")]

    price_usd = get_prices()

    dropdown_change_currency = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#form-currency'))
    )

    ActionChains(browser).move_to_element(dropdown_change_currency).pause(1).click().perform()

    euro = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#form-currency > div > ul > li:nth-child(1) > a'))
    )
    
    euro.click()

    WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".price-new"), "€")
    )

    price_euro = get_prices()

    dropdown_change_currency = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#form-currency'))
    )
    ActionChains(browser).move_to_element(dropdown_change_currency).click().perform()

    gbp = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#form-currency > div > ul > li:nth-child(2) > a'))
    )
    
    gbp.click()
    
    WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".price-new"), "£")
    )

    price_gbp = get_prices()

    assert price_euro != price_gbp != price_usd     

def test_opencart_scenario_4_change_currency_catalog(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog/smartphone")

    def get_prices():
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
        )
        return [float(price.text.replace('€', '').replace('£', '').replace('$', '').strip()) 
                for price in browser.find_elements(By.CSS_SELECTOR, ".price-new")]

    price_gbp = get_prices()

    dropdown_change_currency = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#form-currency'))
    )

    ActionChains(browser).move_to_element(dropdown_change_currency).pause(1).click().perform()

    euro = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#form-currency > div > ul > li:nth-child(1) > a'))
    )
    
    euro.click()

    WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".price-new"), "€")
    )

    price_euro = get_prices()

    dropdown_change_currency = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#form-currency'))
    )
    ActionChains(browser).move_to_element(dropdown_change_currency).click().perform()

    usd = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 
    '#form-currency > div > ul > li:nth-child(3) > a'))
    )
    
    usd.click()
    
    WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".price-new"), '$')
    )

    price_usd = get_prices()

    assert price_euro != price_gbp != price_usd  

